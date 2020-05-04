"""app/sandbox/views/handler.py
"""
from flask import Blueprint, jsonify

from common.utility import err_response

sandbox = Blueprint(
    name='sandbox', import_name=__name__, url_prefix='/sandbox')


@sandbox.route('/healthcheck', methods=['GET'])
def healthcheck():
    """healthcheck
    """
    return jsonify({
        'status': 'healthy',
        'assigned_to': 'feedback-api'
    }), 200


@sandbox.errorhandler(404)
@sandbox.errorhandler(500)
def errorhandler(error):
    """errorhandler
    """
    return err_response(error=error), error.code
