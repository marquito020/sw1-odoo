from odoo import models, fields

class Aula(models.Model):
    _name = 'mi_modulo_academico.aula'
    _description = 'Aula'

    name = fields.Char(string='Nombre', required=True)
    numero = fields.Integer(string='Número de Aula', required=True)
