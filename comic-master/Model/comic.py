from sqlalchemy import Table,MetaData,func
from app import db

class Comic(db.Model):
    __table__ = Table('comic',MetaData(bind=db.engine),autoload=True)

    def get_comic_by_pk(self,pk):
        select_comic = db.session.query(Comic).filter(Comic.id == pk).first()
        db.session.close()
        return select_comic

    def get_comic_list_by_name(self,name):
        print(name)
        if not name:
            return '输入不能为空'
        name = name+"%"
        select_comic = db.session.query(Comic).filter(Comic.name.like(name))
        db.session.close()
        return select_comic


