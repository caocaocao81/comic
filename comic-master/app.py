from flask import Flask, render_template, url_for, flash
from flask import request,session,g,redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__,static_url_path='/')
app.config['SECRET_KEY'] = "dsadsaffds"  # 设置生成session ID
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/ss_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # 实例化对象

# 标签
labels = ['少女漫画','热血漫画','穿越漫画','完结漫画','修仙漫画','黑白漫画','韩国漫画','全彩漫画',
          '惊悚漫画']

img = [1,2,3,4,5,6]

@app.template_global()
def get_comic_like(id):
    redis = Redis.Re()
    count = redis.get_comic_like(id)
    print(count)
    if not count:
        return 0
    return count

@app.template_global()
def get_comic_list11():
    com = comic.Comic()
    comic_list = com.get_cList_only_11()  # 随机获取11个漫画
    return comic_list

@app.template_global()
def get_user_like():
    redis = Redis.Re()
    username = get_username()
    if username:
        return redis.get_user_like(username)
    return None


@app.template_global()
def get_user_view():
    redis = Redis.Re()
    username = get_username()
    if username:
        return redis.get_user_view(username)
    return None


@app.template_global()
def get_username():
    if 'username' in session:
        return session['username']
    return None

@app.template_global()
def get_labels():
    return labels

@app.template_global()
def get_img():
    return img


@app.template_global()
def get_comic_top_list():
    comi = comic.Comic()
    return comi.get_cList_orderBy_lC()


@app.route('/')
def index():
    return render_template('index.html',labels=labels)

@app.route('/regist',methods=['GET','POST'])
def regist():
    if request.method == 'POST':
        re_username = request.form.get('re_name',None)
        re_password = request.form.get('re_password',None)
        re_email = request.form.get('re_email',None)
        re_password_check = request.form.get('re_password_check',None)
        notice = user.User.user_insert(user.User(),re_username,
                                        re_password,re_password_check,re_email)
        flash(notice)
        if notice == "注册成功":
            # session.clear()
            return render_template('login.html',notice=notice)
        else:
            return render_template('login.html',notice=notice)
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    notice = ""
    # session.clear()
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        password = request.form.get('user_password', None)
        vcode = request.form.get('user_vcode',None)
        session['username'] = username
        notice = user.User.validate(user.User(),username,password,vcode)
        # 设置十分钟的session存在时间
        if notice == '登录成功':
            print('登录成功!!!')
            return render_template('index.html',username=username,labels=labels)
        else:
            flash(notice)
            return render_template('login.html',notice=notice)
    else:
        session.clear()
        return render_template('login.html',notice=notice)

@app.route('/ca')
def ca():
    return render_template('a.html')

if __name__ == '__main__':
    from Model import user,comic,comment,Redis
    from Control import commic_control,comment_control,user_control,admin_control
    app.register_blueprint(comment_control.comment)
    app.register_blueprint(commic_control.comc)
    app.register_blueprint(user_control.user)
    app.register_blueprint(admin_control.admin)

    app.run(debug=True,host='127.0.0.1',port=3399)


