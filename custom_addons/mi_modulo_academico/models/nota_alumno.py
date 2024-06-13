from odoo import models, fields

class NotaAlumno(models.Model):
    _name = 'mi_modulo_academico.nota_alumno'
    _description = 'Nota de Alumno'

    alumno_id = fields.Many2one('res.partner', string='Alumno', required=True)
    curso_id = fields.Many2one('mi_modulo_academico.curso', string='Curso', required=True)
    materia_id = fields.Many2one('mi_modulo_academico.materia', string='Materia', required=True)
    profesor_id = fields.Many2one('mi_modulo_academico.profesor', string='Profesor', required=True)
    examen_id = fields.Many2one('mi_modulo_academico.examen', string='Examen', required=True)
    ponderacion = fields.Float(string='Ponderación', required=True)
    boletin_id = fields.Many2one('mi_modulo_academico.boletin_alumno', string='Boletín de Alumno')
