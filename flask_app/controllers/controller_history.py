from flask import render_template, session, request, redirect
from flask_app import app

# MUST import model but make sure you change the name!!
from flask_app.models.model_history import History

# display route