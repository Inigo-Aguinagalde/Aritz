# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class plaiaundi(models.Model):
#     _name = 'plaiaundi.plaiaundi'
#     _description = 'plaiaundi.plaiaundi'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class asignaturas(models.Model):
    _name= 'asignaturas'

    name= fields.Char(string='nombre')
    profesor = fields.Char(string='profesor')
    ciclo = fields.Char(string='ciclo')
    id = fields.Id()


class ciclos(models.Model):
    _name='ciclos.ciclos'

    name=fields.Char(string='ciclos')
    ciclos_id = fields.Id()
    aula=fields.Many2one('aulas.aula','aula_id')
    
class alumnos(models.model):
    _name='alumnos.alumno'

    alumnos_id=fields.id();
    nombre=fields.Char(string='nombre')
    apellido=fields.Char(string='nombre')
    ordenadores=fields.Many2one('ordenadores.ordenador','ordenadores_id',required=True)


class ordenadores(models.Model):
    _name='ordenadores.ordenador'
     
    ordenadores_id=fields.id();
    ocupado=fields.Selection( [('Ocupado', 'Ocupado'),('Libre', 'Libre'),('Reparando','Reparando')],'Asignacion', default='Libre')
    alumnos=fields.One2many('alumnos','alumnos_id')
    aula=fields.One2many('aulas.aula','aula_id')

class aulas():
    _name='aulas.aula'

    aula_id=fields.id();
    nombre=fields.Char(string='nombre');
    ciclo=fields.one2many('ciclos.ciclo','ciclos_id')
