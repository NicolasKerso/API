# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:38:20 2022

@author: leleu
"""

from flask import *
from flask_swagger_ui import get_swaggerui_blueprint
app= Flask(__name__)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
from app import views