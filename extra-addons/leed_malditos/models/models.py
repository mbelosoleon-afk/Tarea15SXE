# -*- coding: utf-8 -*-
# Indica la codificación para Odoo, es como el doctype,
# en python3 ya no es necesario pero scaffold lo deja por convención

# Importamos los modelos, los campos y la api
from odoo import models, fields, api

# todas nuestras clases heredarán de la clase models.Model
class leed_malditos(models.Model):
    #De aquí es de donde cogerá oddo el nombre para la tabla en la BBDD
    #Comprueba los nombres de otros módulos y sus tablas
    #Sigue la estructura modelo.modelo
    _name = 'leed_malditos.leed_malditos'
    #Aquí podemos añadir una pequeña descripción de lo que queremos
    _description = 'Registro de veces que un profesor manda leer'

    #Ahora añadimos los campos a nuestra tabla
    profesor = fields.Char(string="Nombre del docente")
    veces_mando_leer = fields.Integer(string="Veces que mandó leer")