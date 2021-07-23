from flask import Flask, render_template,url_for
from flask import request,session,g,redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__,static_url_path='/')
app.config['SECRET_KEY'] = "dsadsaffds"  # 设置生成session ID
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/ss_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # 实例化对象

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regist',methods=['GET','POST'])
def regist():
    notice = ""
    if request.method == 'POST':
        re_username = request.form.get('re_name',None)
        re_password = request.form.get('re_password',None)
        re_email = request.form.get('re_email',None)
        re_password_check = request.form.get('re_password_check',None)
        notice = user.User.user_insert(user.User(),re_username,
                                        re_password,re_password_check,re_email)
        if notice == "注册成功":
            session.clear()
            return render_template('login.html',notice=notice)
        else:
            return render_template('login.html',notice=notice)

@app.route('/login',methods=['GET','POST'])
def login():
    notice = ""
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        password = request.form.get('user_password', None)
        session['username'] = username
        # 设置十分钟的session存在时间
        if username == 'ccc' and password == '123':
            print('登录成功!!!')
            return render_template('index.html')
        else:
            notice = '登录失败'
    return render_template('login.html',notice=notice)


if __name__ == '__main__':
    from Model import user,comic,comment
    from Control import commic_control,comment_control,user_control
    app.register_blueprint(comment_control.comment)
    app.register_blueprint(commic_control.comc)
    app.register_blueprint(user_control.user)

    app.run(debug=True,host='127.0.0.1',port=3399)


