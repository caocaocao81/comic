import random

from sqlalchemy import Table,MetaData,func
from app import db
from Model import Redis

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

    def get_cList_orderBy_lC(self):
        comicList = db.session.query(Comic).order_by(Comic.like_count.desc()).all()  # 根据like_count 降序排序 desc()降序排序
        db.session.close()
        return comicList

    def get_cList_only_11(self):  # 随机获取11个漫画
        comic_list = db.session.query(Comic).order_by(func.rand()).limit(11).all()  # 随机获取漫画
        db.session.close()
        return comic_list


if __name__ == '__main__':
    c = Comic()
    print(c.get_cList_only_11())