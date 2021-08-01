
from flask import Blueprint,render_template,url_for,request,abort,session
from Model import Redis
from Model.comic import *
comc = Blueprint('commic',__name__)

@comc.route('/comic/<int:pk>/')
def comic(pk):
    c = Comic()
    comic_all = c.get_comic_by_pk(pk)  # 获取漫画
    flag = Redis.Re().if_user_like(session['username'],comic_all)
    return render_template('comic.html',comic=comic_all,flag=flag)

@comc.route('/comic/list/<int:page>',methods=['GET','POST'])
def get_comic_list(page=None):
    if not page:
        page = 1
    comic_name = request.args.get('comic_name', None)
    comic_list = Comic().get_comic_list_by_name(comic_name)
    if type(comic_list) == str:
        return render_template('a.html',comic_list=None,page=None,comic_name=comic_name)
    paginate = comic_list.paginate(page, 10, error_out=False)  # 分页功能 page是指第几页 10是指一页多少条数据
    return render_template('a.html',comic_list=paginate.items,page=paginate,comic_name=comic_name)
    # return render_template('a.html',page=page,comic_list=pagi.items)


#点赞 取消点赞
@comc.route('/comic/like/')
def user_like_or_not():
    img = request.args.get('img')
    print(img)
    # img = 'images/cont/slider-1.jpg'
    id = request.args.get('id')
    comic_name = request.args.get('comicname')
    flag = Redis.Re().set_user_like(id,img,comic_name,session['username'])  # 删除成功或者增加成功为1 反之为0
    print(flag)
    return str(flag)
