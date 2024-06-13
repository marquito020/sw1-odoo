from odoo import models, fields

class Examen(models.Model):
    _name = 'mi_modulo_academico.examen'
    _description = 'Examen'

    materia_id = fields.Many2one('mi_modulo_academico.materia', string='Materia', required=True)
    profesor_id = fields.Many2one('mi_modulo_academico.profesor', string='Profesor', required=True)
    fecha = fields.Date(string='Fecha', required=True)
