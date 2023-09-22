
from odoo import models, fields


class Hospital_Doctor(models.Model):

    _name = 'hospital.doctors'
    # _rec_name = 'first_name'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    image = fields.Binary()
    phone = fields.Char(string='Phone', required=True)




    