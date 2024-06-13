from odoo import models, fields

class Horario(models.Model):
    _name = 'mi_modulo_academico.horario'
    _description = 'Horario'

    name = fields.Char(string='Nombre', required=True)
    hora_inicio = fields.Float(string='Hora de Inicio', required=True)
    hora_fin = fields.Float(string='Hora de Fin', required=True)
