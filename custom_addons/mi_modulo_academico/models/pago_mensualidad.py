from odoo import models, fields

class PagoMensualidad(models.Model):
    _name = 'mi_modulo_academico.pago_mensualidad'
    _description = 'Pago de Mensualidad'

    alumno_id = fields.Many2one('res.partner', string='Alumno', required=True)
    monto = fields.Float(string='Monto', required=True)
    mes = fields.Selection([
        ('enero', 'Enero'),
        ('febrero', 'Febrero'),
        ('marzo', 'Marzo'),
        ('abril', 'Abril'),
        ('mayo', 'Mayo'),
        ('junio', 'Junio'),
        ('julio', 'Julio'),
        ('agosto', 'Agosto'),
        ('septiembre', 'Septiembre'),
        ('octubre', 'Octubre'),
        ('noviembre', 'Noviembre'),
        ('diciembre', 'Diciembre'),
    ], string='Mes', required=True)
    nit = fields.Char(string='NIT', required=False)
