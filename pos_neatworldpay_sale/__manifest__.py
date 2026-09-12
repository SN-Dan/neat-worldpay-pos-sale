# -*- coding: utf-8 -*-
# Original Author: Daniel Stoynev
# Copyright (c) 2025 SNS Software Ltd. All rights reserved.
{
    'name': 'Worldpay PoS Sale/Invoice Payments',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Worldpay Sale Order & Invoice Terminal Payments',
    'description': 'Pay sale orders and invoices with Worldpay POS terminals - depends on PoS Terminal Payment Integration Worldpay',
    'website': 'https://www.sns-software.com',
    'author': 'SNS Software LTD',
    'maintainer': 'SNS Software LTD',
    'depends': ['pos_neatworldpay', 'sale', 'account', 'payment', 'account_payment'],
    'data': [
        'security/ir.model.access.csv',
        'data/payment_provider_data.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/worldpay_terminal_payment_templates.xml',
        'wizard/worldpay_terminal_wizard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'pos_neatworldpay_sale/static/src/css/worldpay_terminal_wizard.css',
        ],
    },
    'images': ['static/description/main.gif'],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
