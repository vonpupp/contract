# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase

from odoo.addons.website_portal_contract.controllers.main import WebsiteAccount
from odoo import http

from mock import patch

MOCK_CONTROL = 'odoo.addons.website_portal_contract.controllers.main.'\
               'WebsiteAccount'


class TestWebsiteAccount(TransactionCase):

    def setUp(self):
        super(TestWebsiteAccount, self).setUp()
        self.controller = WebsiteAccount()
        self.account = self.env.ref(
            'website_portal_contract.account_analytic_account_1'
        )
        self.contract = self.env.ref(
            'website_portal_contract.account_analytic_contract_1'
        )
        self.template = self.env.ref(
            'website_portal_contract.website_contract_template_default'
        )
        http.request.website = self.env.ref(
            'website.default_website',
        )

    @patch('%s._search_contracts' % MOCK_CONTROL)
    def test_account(self, method):
        """ Test updates qcontext with contract count """
        method.return_value = self.contract
        res = self.controller.account()
        self.assertEquals(
            res.qcontext['contract_count'],
            1,
        )
