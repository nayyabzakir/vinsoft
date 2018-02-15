# -*- coding: utf-8 -*- 
from odoo import models, fields, api

class PrePrice(models.Model):
	_inherit = 'product.template'

	pre_price = fields.Float(string ="Pre Price")
	curr_rate = fields.Many2one('ecube.currency',string="Currency")


	@api.onchange('curr_rate','pre_price')
	def _change_sale_price(self):
		if self.pre_price > 0:
			self.list_price = self.pre_price * self.curr_rate.rate


class EcubeCurrency(models.Model):
	_name = 'ecube.currency'


	name = fields.Char(string="Name")
	rate = fields.Float(string="Rate")