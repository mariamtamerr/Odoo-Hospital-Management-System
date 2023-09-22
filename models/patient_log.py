

from odoo import models, fields


class Hospital_Patiant_Log(models.Model):
    _name = 'patient.states.logs'

    description = fields.Char()
    patient_id = fields.Many2one('hospital.patient') 

