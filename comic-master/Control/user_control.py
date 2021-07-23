from flask import Blueprint,render_template,url_for
from Model.user import *
user = Blueprint('user',__name__)

@user.route('/',methods=['GET'])
def index():
    pass