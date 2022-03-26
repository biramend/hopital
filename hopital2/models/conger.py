from odoo import models, fields, api
from datetime import date
STATE = [
("brouillon", "Brouillon")
("cour","En cours de validation")
("validate", "Valider")
("refused", "Refuser")

]


class Conger(models.Model):
	_name="hopital.conger"
	_description="Conger"


	start_date = fields.Date(string="Date debut")
	end_date = fields.Date(string="Date Fin")
	number_of_day=fields.Integer(string="Nombre de jour")
	medcin_id = fields.Many2one("hopital.medcin", string="Medcin")
	state = fields.Selection(SATE,default="brouillon")

	@api.onchange("start_date", "end_date")
	def _onchange_number_of_day(self):
		for record in self:
			if record.start_date and record.end_date:
				record.number_of_day = (record.end_date - record.start_date).days

	def actions_holiday_request(self):
		self.sate = "open"