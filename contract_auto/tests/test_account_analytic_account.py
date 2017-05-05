# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestAccountAnalyticAccount(TransactionCase):

    def setUp(self):
        super(TestAccountAnalyticAccount, self).setUp()
        self.Model = self.env['account.analytic.account']
        self.partner = self.env.ref('base.res_partner_2')
        self.product = self.env.ref('product.product_product_2')
        self.product.taxes_id += self.env['account.tax'].search(
            [('type_tax_use', '=', 'sale')], limit=1)
        self.product.description_sale = 'Test description sale'
        self.template_vals = {
            'recurring_rule_type': 'yearly',
            'recurring_interval': 12345,
            'name': 'Test Contract Template',
            'is_auto_pay': True,
        }
        self.template = self.env['account.analytic.contract'].create(
            self.template_vals,
        )
        self.contract = self.Model.create({
            'name': 'Test Contract',
            'partner_id': self.partner.id,
            'pricelist_id': self.partner.property_product_pricelist.id,
            'recurring_invoices': True,
            'date_start': '2016-02-15',
            'recurring_next_date': '2016-02-29',
        })
        self.contract_line = self.env['account.analytic.invoice.line'].create({
            'analytic_account_id': self.contract.id,
            'product_id': self.product.id,
            'name': 'Services from #START# to #END#',
            'quantity': 1,
            'uom_id': self.product.uom_id.id,
            'price_unit': 100,
            'discount': 50,
        })
