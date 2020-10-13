import os
from flask import current_app


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'