"""app/feedback/views/app.py
"""
from flask import jsonify, render_template


def handler(req):
    """handler
    """
    param1 = req.get('param1')
    param2 = req.get('param2')

    if param1 == 'app_form':
        return _app_form(req=param2)

    return jsonify({'message': 'no route matched with those values'}), 200


def _app_form(req):
    """_app_form
    """
    if req.get('secret_key', '') != 'M7XvWE9fSFg3':
        return jsonify({'message': 'no route matched with those values'}), 200

    url = req.get('url', 'http://0.0.0.0:5000/feedback/api')
    service = req.get('service', '')
    title = req.get('title', '')
    return render_template('app_form.html', url=url, service=service, title=title)
