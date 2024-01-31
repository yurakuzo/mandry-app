import os
from enum import Enum


class Config(Enum):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = bool(os.environ.get('DEBUG'))
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split()

    APP_PORT = os.environ.get('APP_PORT')

    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'db')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'proj_db')
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'proj_usr')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')

    POSTGRES_EXTERNAL_URL = os.environ.get('POSTGRES_EXTERNAL_URL')
