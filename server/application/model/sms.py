#!/usr/bin/env python
# encoding: utf-8
from datetime import datetime

from application.extentions import db


class Sms(db.Model):
    __tablename__ = "sms"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=False, index=True)
    message = db.Column(db.String(140), nullable=False)
    done = db.Column(db.Boolean)
    date_added = db.Column(db.TIMESTAMP, default=datetime.now)

    def __repr__(self):
        return '<{}: {}>'.format(self.phone, self.message[:10])

    def to_json(self):
        return {
            'id': self.id, 'phone': self.phone, 'msg': self.message,
            'create_at': self.date_added.strftime('%Y-%m-%d %H:%M:%S')
        }
