"""app/feedback/views/api.py
"""
from flask import jsonify

from feedback.models import db
from feedback.models.t_feedback import Feedback, upsert_stmt


def handler(req):
    """handler
    """
    param1 = req.get('param1')
    param2 = req.get('param2')

    if param1 == 'read_all':
        return _read_all()

    if param1 == 'read_one':
        return _read_one(record_id=param2)

    if param1 == 'upsert':
        return _upsert(payloads=param2)

    if param1 == 'update':
        return _update(payload=param2)

    if param1 == 'delete':
        return _delete(record_id=param2)

    return jsonify({'message': 'no route matched with those values'}), 200


def _read_all():
    """_read_all
    """
    records = Feedback.query.all()
    return jsonify([record.to_dict() for record in records]), 200


def _read_one(record_id=None):
    """_read_one
    """
    record = Feedback.query.filter_by(id=record_id).first()
    return jsonify(record.to_dict()), 200


def _upsert(payloads):
    """_upsert
    """
    db.session.execute(clause=upsert_stmt(), params=payloads)
    db.session.commit()

    response = jsonify(payloads[-1])
    response.headers['Location'] = \
        '/feedback/api?service=feedback&request=read_one&id={}'.format(
            payloads[-1].get('id'))
    return response, 201


def _update(payload):
    """_update
    """
    record = Feedback.query.filter_by(id=payload.get('id')).first()
    record.set_attrs(payload)

    db.session.commit()

    response = jsonify(None)
    response.headers['Length'] = 0
    return response, 204


def _delete(record_id=None):
    """_delete
    """
    record = Feedback.query.filter_by(id=record_id).first()

    db.session.delete(record)
    db.session.commit()

    response = jsonify(None)
    response.headers['Length'] = 0
    return response, 204
