import hashlib
from flask import Blueprint, request, session, redirect, make_response, render_template, url_for
from util.db import check_login, create_user
from util.auth import authenticated, create_token

api = Blueprint('api', __name__)

@api.route('/logout', methods=['GET'])
@authenticated
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('token', '')
    return response

@api.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if check_login(username, hashlib.md5(password.encode('ascii')).hexdigest()):
        response = make_response(redirect(url_for('index')))
        response.set_cookie('token', create_token(username))
        return response
    return render_template('login.html', err=True, msg="Invalid credentials!")

@api.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    if create_user(username, hashlib.md5(password.encode('ascii')).hexdigest()):
        response = make_response(redirect(url_for('index')))
        response.set_cookie('token', create_token(username))
        return response
    return render_template('register.html', err=True, msg="Unable to create user!")
