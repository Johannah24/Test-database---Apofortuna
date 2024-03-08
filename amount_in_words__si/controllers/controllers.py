# -*- coding: utf-8 -*-
# from odoo import http


# class AmountInWordsSi(http.Controller):
#     @http.route('/amount_in_words__si/amount_in_words__si', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/amount_in_words__si/amount_in_words__si/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('amount_in_words__si.listing', {
#             'root': '/amount_in_words__si/amount_in_words__si',
#             'objects': http.request.env['amount_in_words__si.amount_in_words__si'].search([]),
#         })

#     @http.route('/amount_in_words__si/amount_in_words__si/objects/<model("amount_in_words__si.amount_in_words__si"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('amount_in_words__si.object', {
#             'object': obj
#         })
