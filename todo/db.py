from flask_sqlalchemy import SQLAlchemy 

globaldb = None

def get_db():
    global globaldb
    if globaldb is not None:
        return globaldb
        
def init_db(app):
    db = SQLAlchemy(app)
    global globaldb
    globaldb = db
    return globaldb

def init_app(app):
    db = init_db(app)
    return db