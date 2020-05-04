"""app/config/production.py
"""
import os

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY', '')
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY', '')
JSON_AS_ASCII = False

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', '')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_size': int(os.getenv("SQLALCHEMY_POOL_SIZE", '5')),
    'max_overflow': int(os.getenv("SQLALCHEMY_MAX_OVERFLOW", '10')),
    'pool_timeout': int(os.getenv("SQLALCHEMY_POOL_TIMEOUT", '30'))
}
