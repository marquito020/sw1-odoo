from odoo import models, fields

class Inscripcion(models.Model):
    _name = 'mi_modulo_academico.inscripcion'
    _description = 'Inscripción'

    persona_id = fields.Many2one('res.partner', string='Persona', required=True)
    curso_id = fields.Many2one('mi_modulo_academico.curso', string='Curso', required=True)
    fecha_inscripcion = fields.Date(string='Fecha de Inscripción', required=True)
    lead_id = fields.Many2one('crm.lead', string='Lead CRM')
