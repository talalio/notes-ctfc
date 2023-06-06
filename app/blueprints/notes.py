from flask import Blueprint, session, redirect, url_for, render_template, request
from util.auth import authenticated
from util.db import add_notes, get_notes, del_notes
from util.auth import get_username

notes = Blueprint('notes', __name__)

@notes.route('/list', methods=['GET'])
@authenticated
def notes_list():
    username = get_username()
    return get_notes(username)

@notes.route('/add', methods=['POST'])
@authenticated
def add_note():
    title = request.form['note_title']
    content = request.form['note_content']

    username = get_username()
    add_notes(username, title, content)
    return redirect(url_for('index'))

@notes.route('/del', methods=['POST'])
@authenticated
def del_note():
    if "id" in request.form:
        try:
            note_id = int(request.form['id'])
            del_notes(get_username(), note_id)
        except:
            pass
    return redirect(url_for("index"))