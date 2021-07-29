
from flask import Blueprint,render_template,url_for,request,abort

from Model.comic import *
comc = Blueprint('commic',__name__)

@comc.route('/comic/<int:pk>/')
def comic(pk):
    c = Comic()
    comic_all = c.get_comic_by_pk(pk)
    print(comic_all)
    return render_template('comic.html',comic=comic_all)

@comc.route('/comic/list/<int:page>',methods=['GET','POST'])
def get_comic_list(page=None):
    if not page:
        page = 1
    comic_name = request.args.get('comic_name', None)
    comic_list = Comic().get_comic_list_by_name(comic_name)
    print(comic_list)
    if type(comic_list) == str:
        return abort(404)
    paginate = comic_list.paginate(page, 3, error_out=False)
    print(paginate.items)
    return render_template('a.html',comic_list=paginate.items,page=paginate,comic_name=comic_name)
    # return render_template('a.html',page=page,comic_list=pagi.items)
