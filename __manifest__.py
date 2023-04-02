# -*- coding: utf-8 -*- 


{
    'name': 'Package with product weight',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.2',
    'category': 'Stock',
    'demo': [],
    'depends': ['stock_quant_package_product_unique','prepress_management'],
    'data': [
        'views/stock_quant_views.xml',
        'data/gram_weight_data_migration.sql'
    ],
    'license': 'LGPL-3',
}
