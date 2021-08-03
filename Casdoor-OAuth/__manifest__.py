# -*- coding: utf-8 -*-
{
    'name': "Casdoor OAuth",

    'summary': """OAuth plugin for Odoo by Casdoor""",

    'description': """
        It uses Casdoor's OAuth feature to log in Odoo for convenience.
    """,

    'author': "ffyuanda",
    'website': "https://github.com/casdoor/odoo-casdoor-oauth",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
