

{

'name': 'Hospital',
'version' : '1.0.0',
'category': 'Hospital',
'author': 'Mariam Tamer',
# 'depends': ['base','crm', 'sale'],
'data' : [
   'security/res_groups.xml',
    'security/ir.model.access.csv',
    'views/patient.xml',
    'views/department.xml',
    'views/doctor.xml',
    # 'views/customer.xml',
    'reports/hms_patient_template.xml',
        'reports/reports.xml'
        ],
'images': ['static/description/icon.png'],
'sequence': -10000,
'application': True,
'auto_install': False,
# 'license': 'LGPL-3',
 



}













