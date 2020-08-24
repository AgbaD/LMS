#!/usr/bin/python
# Author:   @BlankGodd_

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .models import User
from flask import current_app

def password_gen(password):
    password_hash = generate_password_hash(password)
    return password_hash

def validate_pass(user, password):
    return check_password_hash(user.password_hash, password)

def gen_cash_id(user_id):
    cash_id = []
    user_id = str.encode(str(user_id))
    while len(cash_id) < 10:
        hashh = generate_password_hash(user_id)
        idd = []
        for i in hashh:
            try:
                idd.append(int(i))
            except:
                pass
        u = len(idd)
        print(u)
        if u + len(cash_id) > 10:
            a = (u + len(cash_id)) - 10
            b = u-a
            for j in range(b):
                cash_id.append(idd[j])
        else:
            cash_id.extend(idd)
    cash_id = [str(i) for i in cash_id]
    return ''.join(cash_id)

def gen_coin_id(user_id):
    user_id = str.encode(str(user_id))
    return generate_password_hash(user_id)

def gen_confirm_token(user):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)
    return s.dumps({'confirm': user.id})

def confirm_token(user, token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return False
    if data.get('confirm') != user.id:
        return False
    user.confirmed = True
    db.session.add(user)
    db.session.commit()
    return True

