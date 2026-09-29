{
    'name': 'Prácticas EINSA',
    'version': '1.0',
    'summary': 'Módulo para registrar ejercicios y propuestas de tableros',
    'description': 'Módulo de aprendizaje para prácticas profesionales',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/practica_dashboard_views.xml',
    ],
    'installable': True,
    'application': True,
}
