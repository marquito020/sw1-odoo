from odoo import models, fields

class Materia(models.Model):
    _name = 'mi_modulo_academico.materia'
    _description = 'Materia'

    name = fields.Char(string='Nombre', required=True)
    curso_id = fields.Many2one('mi_modulo_academico.curso', string='Curso', required=True)
    aula_id = fields.Many2one('mi_modulo_academico.aula', string='Aula', required=True)
    horario_id = fields.Many2one('mi_modulo_academico.horario', string='Horario', required=True)
    profesor_id = fields.Many2one('mi_modulo_academico.profesor', string='Profesor', required=True)
    boletin_id = fields.Many2one('mi_modulo_academico.boletin_alumno', string='Boletín', required=False)
