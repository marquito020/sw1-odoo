from odoo import models, fields

class Reporte(models.Model):
    _name = 'mi_modulo_academico.reporte'
    _description = 'Reporte'

    curso_id = fields.Many2one('mi_modulo_academico.curso', string='Curso', required=True)
    deudores_ids = fields.Many2many('res.partner', string='Deudores')
