from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
import re


class Hospital_Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hopsital Management System'
    # _rec_name = 'name'

     # sql constraints for the unqiue email part
    _sql_constraints = [
        ('unique_email', 'unique(email)', 'Email must be unique. This one exists!'),
    ]

    name = fields.Char(string='Name', required=True, tracking=True)
    # compute function to compute age from date of birth
    age = fields.Integer(string='Age',compute = '_computer_age', store = True)
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female')], string='Gender', required=True,  tracking=True)
    address = fields.Char(string='Address',  tracking=True)
    phone = fields.Char(string='Phone',  tracking=True)
    email = fields.Char(string='Email',  tracking=True, unique=True) 
    blood_type = fields.Selection(   
        [
            
            ('A+','A+'),
             ('B+', 'B+'),
             ('O', 'O'),
             ('AB','AB')
              
        ],  tracking=True)
    states = fields.Selection([('Undetermined','Undetermined'),('Good','Good'),('Fair','Fair'),('Serious','Serious')], default = 'Undetermined')
    history = fields.Html()
    cr_ratio = fields.Float()
    pcr = fields.Boolean(string='PCR',  tracking=True)
    image = fields.Image(string='Image',  tracking=True) #make it fields.Image instead of fields.Binary bc it will raise errors in reports
    department_id = fields.Many2one('hospital.department',  tracking=True)
    doctor_id = fields.Many2one('hospital.doctors')
    capacity = fields.Integer(related='department_id.capacity')
    states_logs=fields.One2many('patient.states.logs', 'patient_id')
    birth_date=fields.Date()
  





    @api.onchange('age')
    def pcr_checked(self) :
        for rec in self:
            if rec.age < 30 :
                rec.pcr = True
                return{
                    'warning':{
                        'title':('Age changed') ,
                        'message': 'PCR field has been checked because age less than 30 and must fill CR ratio'
                    }
                }  

    @api.onchange('states')
    def create_states_log(self):
        for rec in self:
            vals = {
                'description': f'State changed to {rec.states}',
                'patient_id': rec.id
            }
            rec.env['patient.states.logs'].create(vals)


# # unique email address

#     @api.constrains('email')
#     def _check_unique_email(self):
#         for rec in self:
#             email = self.env['hospital.patient'].search( [ ('name', '=' , rec.name) , ( 'id', '!='  , rec.id)     ] )
#             if email:
#                 raise ValidationError({
#                     'email': 'This email is already used by another patient'
#                 })


# api constrains for the 'valid' email part : 

    @api.constrains('email')
    def _check_valid_email(self):
        for rec in self:
            if self.email:
                match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
                if match==False:
                    raise ValidationError({
                        'email': 'This email is not valid'
                    })

# compute date of birth from age 

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = 1






# id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink


# access.hospital.patient,access_hospital_patient,hms.model_hospital_patient,base.group_user,1,1,1,1
