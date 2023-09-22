from odoo import models, fields


class Hospital_Department(models.Model):
    _name = 'hospital.department'

    department_name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients = fields.One2many(comodel_name='hospital.patient', inverse_name='department_id', string= 'department_id') # points to department_id , so we must write it's string

