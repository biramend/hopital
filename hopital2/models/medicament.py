from datetime import datetime
from odoo import models, fields, api


class Medicament(models.Model):
    _name = "hopital2.medicament"
    _description = "Un medicament"

    name = fields.Char(
        string="Libelle",
    )
    code = fields.Char(
        string="Code",
    )
    utilisation = fields.Html(string="utilisation")
    consultation_ids = fields.Many2many(
        "hopital2.consultation",
        string="Consultation"
    )

   
