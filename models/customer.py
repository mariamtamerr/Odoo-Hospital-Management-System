

# Link patient model with customers model from CRM module by adding a 
# new field in customers model called “related_patient_id” and 
# show this field inside  Misc group within sales and purchase 

# cutomer --> a patient family member / billing contacts for ex

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Hospital_Customer(models.Model):
    # _name = "hospital.customer"
    # _description = "Hospital Customers"

    # _inherit = 'hospital.patient' #  a generic model in Odoo used for managing different types of partners, including customers, suppliers, and contacts
    _inherit = 'res.partner' #  a generic model in Odoo used for managing different types of partners, including customers, suppliers, and contacts
                             # and bc i am using it to add the related patiend field m3ahom
    # related_patient_id = fields.Many2one('hospital.patient')  # aka many customers to one related patient
    related_patient_id = fields.Many2one('hospital.patient')



# I'll use the email unique constraint here in customer and not in patient bc I have to make
# sure here too that customers and patient don't have the same email
# like elmtlob fl point tl taht de : 


#  Add a constraint on CRM customer model which prevents linking patient 
#  with email that is already assigned to a different customer


#     @api.constrains('related_patient_id')
#     def _check_unique_email(self):
            
#         # for rec in self:
#             if self.env['res.partner'].search( [ ('email', '=' , self.rec.related_patient_id.email) ] ):
#             # if rec.email == rec.related_patient_id.email:
#                 raise ValidationError({
#                     'email': 'This email is already used by a customer'
#                 })
            


    
# # ➢ Prevent users to delete any customer linked to a patient (BONUS)

#     @api.constrains('related_patient_id')
#     def prevent_delete_linked_customer(self):
#         for rec in self:
#             if rec.related_patient_id:
#                 raise ValidationError({
#                   'related_patient_id': 'You cannot delete a customer linked to a patient'
#                 })
        