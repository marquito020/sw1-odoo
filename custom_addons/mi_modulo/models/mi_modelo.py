# models/mi_modelo.py
from odoo import models, fields

class MiModelo(models.Model):
    _name = 'mi.modulo'
    _description = 'Mi Modelo Descripción'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
