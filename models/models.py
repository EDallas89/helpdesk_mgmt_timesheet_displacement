# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    displacement = fields.Boolean(string='Desplazamiento')