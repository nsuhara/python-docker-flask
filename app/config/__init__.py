"""app/config/__init__.py
"""
import os

env_config = os.getenv('ENV_CONFIG', 'localhost')
config = 'config.localhost'

if env_config == 'production':
    config = 'config.production'
elif env_config == 'docker':
    config = 'config.docker'
else:
    config = 'config.localhost'
