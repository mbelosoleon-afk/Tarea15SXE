# -*- coding: utf-8 -*-
{
    'name': "leed_malditos",

    'summary': "Módulo para contar las veces que un profesor manda leer a los alumnos",

    'description': """
Desde la creciente tendencia del alumnado a no leer la documentación, apuntes ni cualquier material que requiera más de 15"
de esfuerzo, este módulo permite llevar un conteo de cada ocasión en la que un profesor remite a un alumno a la documentación,
al quedar claro -por la pregunta formulada- que no la ha leído a pesar de estar directamente relacionada con los contenidos.
    """,

    'author': "Daniel Castelao",
    'website': "https://www.danielcastelao.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

