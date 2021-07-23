from flask import Blueprint,render_template,url_for
from Model.comic import *
comc = Blueprint('commic',__name__)