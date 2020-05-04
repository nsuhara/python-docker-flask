"""app/feedback/views/handler.py
"""
from flask import Blueprint, jsonify, request

from common.utility import err_response
from feedback.views.api import handler as api_handler
from feedback.views.app import handler as app_handler

feedback = Blueprint(name='feedback', import_name=__name__,
                     url_prefix='/feedback')


@feedback.route('/healthcheck', methods=['GET'])
def healthcheck():
    """healthcheck
    """
    return jsonify({'status': 'healthy'}), 200


@feedback.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api():
    """api
    """
    if request.method == 'GET':
        process = request.args.get('process')

        if process == 'back_end':
            req = {
                'param1': request.args.get('request'),
                'param2': request.args.get('id', None)
            }
            return api_handler(req=req)

        if process == 'front_end':
            req = {
                'param1': request.args.get('request'),
                'param2': request.args
            }
            return app_handler(req=req)

    if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
        payload = request.json
        process = payload.get('process')
        req = payload.get('request')

        if process == 'back_end':
            return api_handler(req=req)

    return jsonify({'message': 'no route matched with those values'}), 200


@feedback.errorhandler(404)
@feedback.errorhandler(500)
def errorhandler(error):
    """errorhandler
    """
    return err_response(error=error), error.code
