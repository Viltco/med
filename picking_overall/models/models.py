# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPickingInh(models.Model):
    _inherit = 'stock.picking'

    received_by = fields.Char()
    dept_incharge = fields.Char()
    passed_by = fields.Char()
    issued_by = fields.Char()
