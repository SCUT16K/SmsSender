#!/usr/bin/env python
# encoding: utf-8
from flask import request, jsonify
from flask.views import MethodView

from application.extentions import db
from application.model.sms import Sms


class SmsView(MethodView):
    def get(self):
        smses = Sms.query.filter_by(done=False).all()
        if smses:
            return jsonify(**{'messages': [sms.to_json() for sms in smses]})
        else:
            return jsonify(**{})

    def post(self):
        data = request.get_json()
        sms = Sms(phone=data.get('phone'), message=data.get('message'),
                  done=False)
        db.session.add(sms)
        db.session.commit()
        return jsonify(id=sms.id, phone=sms.phone)
