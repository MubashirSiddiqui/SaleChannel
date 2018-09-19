from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning

import logging
_logger = logging.getLogger(__name__)


class CrmTeam(models.Model):
	_inherit = "crm.team"

	#country_id_sale= fields.Many2one("res.country","Country Select")
	test_country_id = fields.Selection([('pakistan', 'Pakistan'),
                                     ('china', 'China')],
                                     string='Country')
	country_id = fields.Many2many('res.country', string='Country', ondelete='restrict')
	
	

	
class SaleOrders(models.Model):
	_inherit="sale.order"
	def _default_country(self):
		_logger.info('------------Im coming here')
		return self.env['res.country'].search([('code', '=', "PK")], limit=1)

	country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=_default_country)
	partner_id = fields.Many2one('res.partner', string='Customer', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always')
	


	#@api.one
	@api.onchange('partner_id')
	def onchange_so_id(self):
		_logger.info('--------Iam raching in partner id')
		_logger.info('-------ANd My country id is %s',self.partner_id.country_id.display_name)
		name_country=self.partner_id.country_id
		#self.env['crm.team'].
		
		country_search=self.env['crm.team'].search([])
		sale_search=self.env['sale.order'].search([])
		self.ensure_one()

		for c in country_search:
			_logger.info('Country record are ------ %s',c)

			for v in c.country_id:
				_logger.info('-------v answer is %s',v.name)
				if v.name==self.partner_id.country_id.display_name:
					_logger.info('-----BEST ')
					_logger.info('-----team id is %s',c.id)
					self.update({
				
			    	'team_id': c.id,
				
				    })
		
		#country_search=self.env['crm.team'].search[('country_id','=',self.partner_id.country_id)]
		#query ="""SELECT id FROM crm_team where id >2;"""
		#query = """SELECT crm_team.id
		#			 FROM crm_team
		#			INNER JOIN res_country ON crm_team.country_id=res_country.id;"""
		#result = self._cr.execute(query)
		
		
		self.update({
				
				#'partner_id': self.so_id.partner_id.id,
				
				})


	



