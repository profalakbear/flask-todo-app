from . import db

DB = db.get_db()

class Todo(DB.Model):
    __tablename__ = 'todos'
    id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(100))
    description = DB.Column(DB.String(200))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return f'{self.title}'