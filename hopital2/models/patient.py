from datetime import datetime

from odoo import models, fields, api


class Patient(models.Model):
    _name = "hopital2.patient"
    _description = "Un patient"

    @api.depends("date")
    def _compute_age(self):
        for record in self:
            if record.date:
                record.age = datetime.now().year - record.date.year
        return None

    name = fields.Char(
        string="Nom",
        required=True,
    )
    lastname = fields.Char(
        string="Prénom",
    )
    date = fields.Date(string="Date de Naissance")
    age = fields.Integer(string="Age", compute="_compute_age")
    consultation_ids = fields.One2many(
        "hopital2.consultation",
        "patient_id",
        string="Consultations",
    )
    email = fields.Char(
        string="Email",
        )
    address=fields.Char(string = "Address")
    
