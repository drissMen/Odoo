# -*- coding: utf-8 -*-
from odoo import fields, models


class pat(models.Model):
    _inherit = 'res.partner'

    assurance = fields.Char(string="Assurance")
    matricule = fields.Char(string="Matricule")
    prescripteur = fields.Char(string="Prescripteur")