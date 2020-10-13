from flask import Flask

def create_app():
	"""Construct the core application."""
	app = Flask(__name__)
	
	with app.app_context():
		app.config.from_object('config.Config')
		
	with app.app_context():
		from . import api

		return app