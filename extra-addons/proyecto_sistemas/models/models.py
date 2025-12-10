# -*- coding: utf-8 -*-

from odoo import models, fields, api
from pkg_resources import require


class proyecto_sistemas(models.Model):
     _name = 'proyecto_sistemas.proyecto_sistemas'
     _description = 'Bebidas recomendadas'

     alumno = fields.Char(required = True)
     nivel_sueno = fields.Integer(
         string='Nivel de Sueno (1-10)',
         required=True,
         default=1,
         help="Indica que tan dormido está el alumno"
     )
     bebida_recomendada = fields.Char(compute="_calcularBebida",store=True)

     @api.depends('nivel_sueno')
     def _calcularBebida(self):
         for record in self:
             nivel = record.nivel_sueno

             if nivel >= 1 and nivel <= 3:
                 record.bebida_recomendada = "Café con leche"
             elif nivel >= 4 and nivel <= 6:
                 record.bebida_recomendada = "Café solo largo"
             elif nivel >= 7 and nivel <= 9:
                 record.bebida_recomendada = "Café solo larguísimo"
             elif nivel == 10:
                 record.bebida_recomendada = "Inyección de adrenalina"
             else:
                 record.bebida_recomendada = "Fuera del rango"

