import os
from flask import Flask, session, render_template
from blueprints.api import api
from blueprints.notes import notes
from util.db import init_flags, get_notes
from util.auth import authenticated, get_username, generate_key

app = Flask(__name__)
app.secret_key = b'nj1289d23'
app.register_blueprint(api, url_prefix='/api/')
app.register_blueprint(notes, url_prefix='/notes/')

@app.route('/', methods=['GET'])
def index():
    notes = None
    username = get_username()
    if username:
        notes = get_notes(username)
    return render_template('index.html', username=username, notes=notes)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/note', methods=['GET'])
@authenticated
def note():
    username = get_username()
    return render_template('note.html', username=username)

def initialize():
    os.environ["FIRST_RUN"] = "False"
    os.environ["JWT_KEY"] = generate_key(16)
    with open('flags.txt', 'r') as ff:
        flags = [flag.strip() for flag in ff.readlines()]
        init_flags(flags[0], flags[1])

if __name__=='__main__':
    if os.environ.get("FIRST_RUN", False):
        initialize()
    port = int(os.environ.get('PORT', 80))
    app.run(debug=False, host='0.0.0.0', port=port)