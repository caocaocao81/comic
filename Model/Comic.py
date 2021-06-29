from sqlalchemy import Table,MetaData,func
from app import db

class comic(db.Model):
    __table__ = Table('comic',MetaData(bind=db.engine),autoload=True)
