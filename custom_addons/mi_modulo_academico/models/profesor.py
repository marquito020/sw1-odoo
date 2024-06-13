from odoo import models, fields

class Profesor(models.Model):
    _name = 'mi_modulo_academico.profesor'
    _description = 'Profesor'

    name = fields.Char(string='Nombre', required=True)
    materia_ids = fields.One2many('mi_modulo_academico.materia', 'profesor_id', string='Materias')
