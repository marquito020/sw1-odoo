{
    'name': 'Gestión Académica',
    'version': '1.0',
    'summary': 'Módulo de gestión académica integrado con CRM y pagos',
    'description': 'Gestión de matrículas, cursos, horarios, evaluaciones, pagos y más.',
    'author': 'Tu Nombre',
    'website': 'http://www.tusitio.com',
    'category': 'Education',
    'depends': ['base', 'crm', 'account', 'web'],
    'data': [
        'security/mi_modulo_academico_security.xml',
        'security/ir.model.access.csv',
        'views/curso_views.xml',
        'views/aula_views.xml',
        'views/horario_views.xml',
        'views/materia_views.xml',
        'views/profesor_views.xml',
        'views/inscripcion_views.xml',
        'views/pago_mensualidad_views.xml',
        'views/examen_views.xml',
        'views/nota_alumno_views.xml',
        'views/boletin_alumno_views.xml',
        'views/reporte_views.xml',
        'views/comunicado_views.xml',
        'views/asistencia_views.xml',
        'views/padre_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
