from flask import Flask, render_template,url_for
from flask import request,session,g,redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__,static_url_path='/')
app.config['SECRET_KEY'] = "dsadsaffds"  # 设置生成session ID
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@8.142.98.163:3306/py_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # 实例化对象

@app.route('/')
def index():
    return render_template('index.html',h='Hello World')

@app.route('/login')
def login():
    return 'hello'


if __name__ == '__main__':
    from Control import commic_control,comment_control,user_control
    app.register_blueprint(comment_control.comment)
    app.register_blueprint(commic_control.comc)
    app.register_blueprint(user_control.user)

    app.run(debug=True,host='127.0.0.1',port=3399)


