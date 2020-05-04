"""app/run.py
"""
import os

from flask import Flask
from flask_migrate import Migrate

from common.utility import err_response
from config import config
from feedback.models import db
from feedback.views.handler import feedback

app = Flask(__name__,
            static_folder='feedback/static',
            template_folder='feedback/templates')
app.config.from_object(config)

app.register_blueprint(feedback)
# add healthcheck for sandbox by nsuhara
try:
    from sandbox.views.handler import sandbox
    app.register_blueprint(sandbox)
except ImportError:
    pass

db.init_app(app)
Migrate(app, db)


@app.errorhandler(404)
@app.errorhandler(500)
def errorhandler(error):
    """errorhandler
    """
    return err_response(error=error), error.code


def main():
    """main
    """
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '5000'))
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()
