# -*- coding: utf-8 -*-
{
    "name": "2020 Philippine Taxes (OmniTechnical)",
    "summary": """
        2020 Philippine Taxes (OmniTechnical)""",
    "description": """
        2020 Philippine Taxes (OmniTechnical) 
    """,
    "author": "OmniTechnical Global Solutions, Inc.",
    "website": "http://www.omnitechnical.com",
    "license" : "OPL-1",
    # Categories can be used to filter modules in modules
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Invoicing",
    "price": 99,
    "currency":"USD" ,
    "version": "1.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale", "l10n_generic_coa", "account"],
    # always loaded
    "data": [
        # 'security/user_groups.xml',
        # 'security/security_data.xml',
        "views/views.xml",
        "data/account_tax.xml",
        "data/account.tax.csv",
    ],
    "qweb": [
        # 'static/src/xml/extend_thread_fields.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
