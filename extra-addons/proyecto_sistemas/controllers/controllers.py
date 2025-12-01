# -*- coding: utf-8 -*-
from odoo import http


class ProyectoSistemas(http.Controller):
    @http.route('/proyecto_sistemas/proyecto_sistemas', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/proyecto_sistemas/proyecto_sistemas/objects', auth='public')
    def list(self, **kw):
        return http.request.render('proyecto_sistemas.listing', {
            'root': '/proyecto_sistemas/proyecto_sistemas',
            'objects': http.request.env['proyecto_sistemas.proyecto_sistemas'].search([]),
        })

    @http.route('/proyecto_sistemas/proyecto_sistemas/objects/<model("proyecto_sistemas.proyecto_sistemas"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('proyecto_sistemas.object', {
            'object': obj
        })

