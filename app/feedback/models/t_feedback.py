"""app/feedback/models/t_feedback.py
"""
from datetime import datetime, timezone

from sqlalchemy.dialects.postgresql import insert

from feedback.models import db


class Feedback(db.Model):
    """feedback transaction model
    """
    __tablename__ = 't_feedback'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=created_at.default)

    def __init__(self, payload):
        self.service = payload.get('service')
        self.title = payload.get('title')
        self.detail = payload.get('detail')

    def set_attrs(self, payload):
        """set_attrs
        """
        for name, value in payload.items():
            if name in self.__dict__:
                setattr(self, name, value)
        setattr(self, 'updated_at', datetime.now(timezone.utc))

    def to_dict(self):
        """to_dict
        """
        return {
            'id': self.id,
            'service': self.service,
            'title': self.title,
            'detail': self.detail,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


def upsert_stmt():
    """upsert_stmt
    """
    stmt = insert(Feedback)
    return stmt.on_conflict_do_update(
        index_elements=['id'],
        set_={
            'service': stmt.excluded.service,
            'title': stmt.excluded.title,
            'detail': stmt.excluded.detail,
            'updated_at': stmt.excluded.updated_at
        })
