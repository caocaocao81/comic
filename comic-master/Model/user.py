from sqlalchemy import func,Table,MetaData
from app import db
from flask import session
import hashlib

class User(db.Model):
    __table__ = Table('user',MetaData(bind=db.engine),autoload=True)

    def insert_user(self,name,pwd,email):
        insert = User(name=name,pwd=pwd,email=email)
        db.session.add(insert)
        db.session.commit()
        db.session.close()

    def select_user_by_name_like(self,name):  # 根据姓名模糊查找
        select_like = db.session.query(User).filter(User.name.like('%'+name+'%')).first()
        db.session.close()
        return select_like

    def updata_user(self,email,photo,pwd):  # 更新用户信息
        try:
            db.session.add(User(email=email,user_photo=photo,pwd=pwd))
            db.session.commit()
        except:
            db.session.rollback()
        db.session.close()

    def check_name_pwd(self,name,pwd):

        a = db.session.query(User).filter(User.name == name,User.pwd == pwd).first()
        db.session.close()
        return a

    # 用户登录返回的提示信息
    def validate(self,username, pwd1,vcode):
        user = self.check_name_pwd(username,pwd1)
        md5 = hashlib.md5()
        try:
            if vcode == session['vcode']:
                if user:
                    # 加密密码
                    md5.update(pwd1.encode('utf-8'))
                    pwd_md5 = md5.hexdigest()
                    if user.pwd == pwd_md5:
                        return '登陆成功'
                    else:
                        return '密码错误'
                else:
                    return '用户名不存在'
            else:
                return '验证码错误'
        except:
            return '未知错误'

    def user_insert(self,name,pwd,pwd1,email):
        users = User()
        md5 = hashlib.md5()
        if pwd != pwd1:
            return "两次密码不一致"
        # 加密密码
        md5.update(pwd.encode('utf-8'))
        pwd_md5 = md5.hexdigest()
        try:  # 添加用户
            users.insert_user(name,pwd_md5,email)
        except:
            return "注册失败请重试"
        else:
            return "注册成功"