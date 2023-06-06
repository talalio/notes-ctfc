import hashlib
import os
from peewee import SqliteDatabase
from .models import User, Note

db = SqliteDatabase('notepad.db')
User.bind(database=db)
Note.bind(database=db)

db.create_tables([User, Note])

def md5hash(string):
    return hashlib.md5(string.encode('ascii')).hexdigest()

def init_flags(flag1, flag2):
    admin = User.create(username='admin', password=md5hash(os.urandom(8).hex()))
    james = User.create(username='james', password=md5hash(os.urandom(8).hex()))
    Note.create(user_id=admin, title='flag', content=f'{flag1}')
    Note.create(user_id=james, title='My Secret', content=f'{flag2}')


def get_notes(uname: str) -> list:
    user = User.get(User.username==uname)
    return [{'id':note.note_id,'title':note.title, 'content':note.content} for note in user.notes]

def add_notes(uname: str, ntitle: str, ncontent: str) -> bool:
    try:
        user = User.get(User.username == uname)
        Note.create(user_id=user, title=ntitle, content=ncontent)
        return True
    except:
        return False

def del_notes(uname: str, nid: int) -> bool:
    try:
        user = User.get(User.username == uname)
        user_notes = [note.note_id for note in user.notes]
        if nid in user_notes:
            Note.delete().where(Note.note_id==nid).execute()
            return True
        return False
    except:
        return False

def create_user(uname: str, upass: str) -> bool:
    try:
        with db.atomic():
            User.create(username=uname, password=upass)
            return True
    except:
        return False

def check_login(uname: str, upass: str) -> bool:
    try:
        User.get(User.username == uname, User.password == upass)
        return True
    except:
        return False
