{
    'name': 'Amount To Text',
    'version': '17.0.1.3.0',
    'author': 'Ganemo',
    'company': 'Ganemo',
    'maintainer': 'Ganemo',
    'support': 'support@ganemo.com',
    'contributors': [
        'Leo Daniel Flores Sánchez <leo.dev.ganemo@gmail.com>',
    ],
    'website': 'https://www.ganemo.co',
    'live_test_url': 'https://www.ganemo.co',
    'category': 'Accounting/Accounting',
    'summary': 'Convert the total amount into letters',
    'description': """
This module creates a function in the "account.move" model that converts the
total amount of the invoice (amount_total) to text in spanish.

This module serves as help to other modules (mostly modules that create invoice reports)
to complete the total amount in letters.
""",
    'depends': [
        'account'
    ],
    'module_type': 'official',
    'application': False,
    'installable': True,
    'auto_install': False,
    'license': 'Other proprietary',
    'currency': 'USD',
    'price': 20.00
}
