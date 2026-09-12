# -*- coding: utf-8 -*-
from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('neatworldpaypos', "Worldpay Sales POS")],
        ondelete={'neatworldpaypos': 'set default'},
    )
