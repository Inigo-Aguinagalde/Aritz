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
    _name= 'asignaturas.asignatura'

    name= fields.Char(string='nombre')
    profesor = fields.Char(string='profesor')
    ciclo = fields.Many2one(string='ciclos.ciclo')




class ciclos(models.Model):
    _name='ciclos.ciclo'

    name=fields.Char(string='ciclos')
    aula=fields.Many2one('aulas.aula','ciclo')
    asignatura=fields.One2Many('asignaturas.asignatura','ciclos',string="ciclos")

class alumnos(models.model):
    _name='alumnos.alumno'

    nombre=fields.Char(string='nombre')
    apellido=fields.Char(string='nombre')
    ordenadores=fields.Many2one('ordenadores.ordenador','alumnos',required=True)
    faltas=fields.Int(String="faltas")
    nota=fields.Float(String="notas")


class ordenadores(models.Model):
    _name='ordenadores.ordenador'
     
    ocupado=fields.Selection( [('Ocupado', 'Ocupado'),('Libre', 'Libre'),('Reparando','Reparando')],'Asignacion', default='Libre')
    alumnos=fields.One2many('alumnos.alumno','ordenadores')
    aula=fields.One2many('aulas.aula','ordenadores')

class aulas():
    _name='aulas.aula'

    nombre=fields.Char(string='nombre')
    ciclo=fields.one2many('ciclos.ciclo')
    ordenadores=fields.Many2One('ordenadores.ordenador','aula')
