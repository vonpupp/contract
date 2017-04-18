# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import json

from odoo import http
from odoo.http import request

from odoo.addons.website_portal_sale.controllers.main import website_account


class WebsiteAccount(website_account):

    @http.route()
    def account(self, **kw):
        response = super(WebsiteAccount, self).account(**kw)
        response.qcontext.update({
            'contract_count': len(self._search_contracts()),
        })
        return response

    @http.route(
        ['/my/contracts'],
        type='http',
        auth='user',
        website=True
    )
    def portal_my_contracts(self):
        values = {
            'user': request.env.user,
            'contracts': self._search_contracts(),
        }
        return request.render(
            'website_portal_contract.portal_my_contracts',
            values
        )

    @http.route(
        ['/contract/<int:id>'],
        type='http',
        auth='user',
        website=True
    )
    def portal_contract(self, **kwargs):
        rec_id = kwargs.get('id')
        if not rec_id:
            return json.dumps(False)
        contract = request.env['account.analytic.account'].browse(rec_id)
        action = request.env.ref(
            'contract.action_account_analytic_overdue_all'
        ).id
        values = {
            'user': request.env.user,
            'contract': contract,
            'action': action,
            'invoices': contract.recurring_invoice_line_ids.ids,
        }
        return request.render(
            'website_portal_contract.website_contract',
            values
        )

    @http.route(
        ["/contract/template/"
         "<model('account.analytic.contract.template'):contract>"],
        type='http',
        auth='user',
        website=True
    )
    def template_view(self, contract):
        values = {'template': contract}
        return request.render(
            'website_portal_contract.website_contract_template',
            values,
        )

    def _search_contracts(self):
        partner = request.env.user.partner_id
        contract_mod = request.env['account.analytic.account']
        contracts = contract_mod.search([
            ('message_partner_ids', 'child_of',
             [partner.commercial_partner_id.id]),
            ('recurring_invoices', '=', True)
        ])
        return contracts
