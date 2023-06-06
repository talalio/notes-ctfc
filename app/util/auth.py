import jwt
import os
from flask import redirect, request, url_for
from functools import wraps

JWT_KEY = os.environ.get("JWT_KEY", os.urandom(16).hex())

def generate_key(key_length):
    return os.urandom(key_length).hex()

def authenticated(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.cookies.get('token')
        if not verify_token(token):
             return redirect(url_for('login'))

        return f(*args, **kwargs)
    
    return decorator

def verify_token(token):
    try:
        jwt.decode(token, algorithms=['none', 'HS256'], options={'verify_signature':False})
        return True
    except:
        return False

def create_token(username):
    return jwt.encode({"username":f"{username}"}, key=JWT_KEY, algorithm="HS256")

def get_username():
    try:
        token = request.cookies.get('token')
        data = jwt.decode(token, key=JWT_KEY, algorithms='HS256', options={'verify_signature':False})
        return data['username']
    except:
        return None