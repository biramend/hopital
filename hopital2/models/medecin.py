from datetime import datetime
from odoo import models, fields, api


class Medecin(models.Model):
    _name = "hopital2.medecin"
    _description = "Un medecin"

    matricule = fields.Char(
        string="Matricule",
    )
    name = fields.Char(
        string="Nom",
    )
