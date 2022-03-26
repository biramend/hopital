# -*- coding: utf-8 -*-

{
    "name": "Mon hopital",
    "version": "13.0.1",
    "category": "HOPITAL2",
    "summary": """
        Resumé de mon module hopital
    """,
    "description": """Description du module""",
    "author": "Tdsi",
    "company": "TDSI",
    "maintainer": "Tdsi",
    "website": "https://www.tdsi.sn",
    "depends": ["base","mail","web"],
    "data": [
        # "security/base_security.xml",
        "security/ir.model.access.csv",
        # "data/auth_signup_data.xml",
        # "data/webclient_templates.xml",
        "views/patient_views.xml",
        "views/medecin_views.xml",
        "views/consultation_views.xml",
        "views/medicament_views.xml",
        "data/hopital_sequences.xml",
        "data/mail_templates.xml",
        "report/hopital_report_templates.xml",
        "report/hopital_reports.xml",
        "report/hopital_report_templates_consultation.xml",
        "report/hopital_reports_consultation.xml",
       
    ],
    "installable": True,
    #'images': ['static/description/banner.png'],
    "auto_install": False,
    "application": False,
    "license": "AGPL-3",
}
