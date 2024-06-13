from odoo import models, fields

class Asistencia(models.Model):
    _name = 'mi_modulo_academico.asistencia'
    _description = 'Asistencia'

    fecha = fields.Date(string='Fecha', required=True)
    alumno_id = fields.Many2one('res.partner', string='Alumno', required=True)
    profesor_id = fields.Many2one('mi_modulo_academico.profesor', string='Profesor', required=True)
