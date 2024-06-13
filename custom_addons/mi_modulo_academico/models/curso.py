from odoo import models, fields

class Curso(models.Model):
    _name = 'mi_modulo_academico.curso'
    _description = 'Curso'

    name = fields.Char(string='Nombre', required=True)
    nivel = fields.Selection([('primaria', 'Primaria'), ('secundaria', 'Secundaria')], string='Nivel', required=True)
    grado = fields.Char(string='Grado', required=True)
    turno = fields.Selection([('mañana', 'Mañana'), ('tarde', 'Tarde')], string='Turno', required=True)
