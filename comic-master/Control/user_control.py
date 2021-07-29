from io import BytesIO
from flask import Blueprint,render_template,url_for,make_response, url_for, request,redirect
from Model.user import *
from Model.img import *
user = Blueprint('user',__name__)

@user.route('/',methods=['GET'])
def index():
    pass

@user.route('/get_img')  # 获得验证码图片
def get_img():
    text, image = Captcha.gene_graph_captcha()
    print(text, image)
    session['vcode'] = text
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp