from odoo import models, fields

class Padre(models.Model):
    _name = 'mi_modulo_academico.padre'
    _description = 'Padre'

    name = fields.Char(string='Nombre', required=True)
    padre_id = fields.Many2one('res.partner', string='Padre', required=True)
    alumno_ids = fields.Many2many('res.partner', string='Alumnos', domain=[('customer_rank', '>', 0)])
