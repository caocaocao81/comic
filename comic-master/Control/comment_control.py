from flask import Blueprint,render_template,url_for
from Model.comment import *
comment = Blueprint('comment',__name__)

@comment.route('/comment/',methods=['GET','POST'])
def AllComment():
    pass