from sqlalchemy import Table,func,MetaData
from app import db

class comment(db.Model):
    __table__ = Table('comment',MetaData(bind=db.engine),autoload=True)
