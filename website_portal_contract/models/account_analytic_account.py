# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountAnalyticAccount(models.Model):

    _inherit = 'account.analytic.account'

    website_template_id = fields.Many2one(
        string='Website Template',
        comodel_name='account.analytic.contract.template',
        help='Website layout for contract',
    )
