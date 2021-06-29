from sqlalchemy import func,Table,MetaData
from app import db

class user(db.Model):
    __table__ = Table('user',MetaData(bind=db.engine),autoload=True)
