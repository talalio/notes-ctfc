from peewee import *

class User(Model):
    user_id = PrimaryKeyField()
    username = CharField(max_length=15, unique=True)
    password = CharField()

    class Meta:
        table_name = 'users'

class Note(Model):
    note_id = PrimaryKeyField()
    user_id = ForeignKeyField(model=User, on_update='CASCADE', backref='notes')
    title = CharField()
    content = TextField()

    class Meta:
        table_name = 'notes'