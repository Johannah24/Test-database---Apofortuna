# -*- coding: utf-8 -*-

from odoo import models, fields, api
from num2words import num2words


class amount_in_words__si(models.Model):
    _inherit = 'account.move'

      check_amount_in_words = fields.Char(
        string="Amount in Words",
        store=False,
        compute="_compute_check_amount_in_words"
    )
    
    def round_amount_to_two_decimals(self, amount):
        """Round off the amount to two decimal places."""
        return round(amount, 2)

    def amount_to_text(self, amount):
        """Return the amount in words."""
        rounded_amount = self.round_amount_to_two_decimals(amount)
        # Get the amount in words with currency as "MXN"
        amount_in_words = num2words(rounded_amount, to='currency', lang='en', currency='MXN')
        # Replace "Centavos" with "Cents"
        amount_in_words = amount_in_words.replace("cents", "centavos")
        return amount_in_words
        

    @api.depends('payment_method_line_id', 'currency_id', 'amount')
    def _compute_check_amount_in_words(self):
        for payment in self:
            payment.check_amount_in_words = payment.amount_to_text(payment.amount)
    
