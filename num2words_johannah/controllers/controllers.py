# -*- coding: utf-8 -*-
# from odoo import http


# class Num2wordsJohannah(http.Controller):
#     @http.route('/num2words_johannah/num2words_johannah', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/num2words_johannah/num2words_johannah/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('num2words_johannah.listing', {
#             'root': '/num2words_johannah/num2words_johannah',
#             'objects': http.request.env['num2words_johannah.num2words_johannah'].search([]),
#         })

#     @http.route('/num2words_johannah/num2words_johannah/objects/<model("num2words_johannah.num2words_johannah"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('num2words_johannah.object', {
#             'object': obj
#         })
