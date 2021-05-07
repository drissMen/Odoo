# -*- coding: utf-8 -*-
from odoo import http


# class PharHerit(http.Controller):
#     @http.route('/phar__herit/phar__herit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phar__herit/phar__herit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('phar__herit.listing', {
#             'root': '/phar__herit/phar__herit',
#             'objects': http.request.env['phar__herit.phar__herit'].search([]),
#         })

#     @http.route('/phar__herit/phar__herit/objects/<model("phar__herit.phar__herit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phar__herit.object', {
#             'object': obj
#         })
