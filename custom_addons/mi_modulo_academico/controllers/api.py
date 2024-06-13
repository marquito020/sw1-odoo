from odoo import http
from odoo.http import request

class MiModuloAcademicoAPI(http.Controller):

    @http.route('/api/cursos', type='json', auth='public', methods=['GET'])
    def get_cursos(self):
        cursos = request.env['mi_modulo_academico.curso'].search([])
        cursos_data = cursos.read(['name', 'nivel', 'grado', 'turno'])
        return {'cursos': cursos_data}

    @http.route('/api/inscripciones', type='json', auth='public', methods=['POST'])
    def create_inscripcion(self, **kwargs):
        inscripcion = request.env['mi_modulo_academico.inscripcion'].create(kwargs)
        return {'id': inscripcion.id}
