# -*- coding: utf-8 -*-
# Copyright 2019 Fenix Engineering Solutions
# @author Jose F. Fernandez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Pagare Printing Base',
    'version': "11.0.1.0.1",
    'category': 'Accounting',
    'summary': 'Pagare printing commons',
    'description': """
This module offers the basic functionalities to make payments by printing pagares.
The pagare settings are located in the accounting journals configuration page.
    """,
    'license': 'AGPL-3',
    'author': "Fenix Engineering Solutions",
    'website': "http://www.fenix-es.com",
    'depends': ['account'],
    'data': [
        'data/account_pagare_printing_data.xml',
        'views/account_journal_views.xml',
        'views/account_payment_views.xml',
        'wizard/print_prenumbered_pagares_views.xml'
    ],
    'installable': True,
    'auto_install': False,
}