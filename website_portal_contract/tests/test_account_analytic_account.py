# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestAccountAnalyticAccount(TransactionCase):

    def setUp(self):
        super(TestAccountAnalyticAccount, self).setUp()
        self.account = self.env.ref(
            'website_portal_contract.account_analytic_account_1'
        )
        self.contract = self.env.ref(
            'website_portal_contract.account_analytic_contract_1'
        )

    def test_website_template_id(self):
        """ Test website_template_id inherited from contract """
        self.assertEquals(
            self.account.website_template_id,
            self.contract.website_template_id,
        )
