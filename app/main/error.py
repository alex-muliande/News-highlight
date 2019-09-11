from flask import render_template
from .import main

@main.app_errorhandler(404)
def fourOwfour(error):
    return render_template('fourOwfour.html'), 404
