"""只处理与主题相关的路由和视图"""
import os

from . import main
from flask import render_template,session,request,redirect
from .. import db
from ..models import *
import datetime

@main.route('/')
def index_viewxs():
    #查询Topic中所有数据并发送到index.html做显示
    topics = Topic.query.limit(10).all()
    # for a in topics:
    #     print(a.title,a.images)
    #读取Catrgories中的所有内容并发送到index.html显示
    categories = Category.query.all()
    #判断是否有登录的用户(判断session中是否有id和loginname)
    # for a in categories:
    #     print(a.cate_name)
    #判断是否有登录的用户
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template("index.html",params=locals())


@main.route('/release',methods=['POST','GET'])
def release_views():
    if request.method == 'GET':
        if 'id' in session and 'loginname' in session:
            id=session['id']
            user=User.query.filter_by(ID=id).first()
            print(user.is_author)
            if user.is_author:
                # 查询Category  BlogType的信息
                categories = Category.query.all()
                blogTypes = BlogType.query.all()
                return render_template('release.html', params=locals())
        return redirect('/')
    else:
        topic = Topic()
        topic.title=request.form['author']
        topic.blogtype_id=request.form['list']
        topic.category_id=request.form['category']
        topic.content=request.form['content']
        topic.user_id=session['id']
        #获取系统时间为topic.pub_date赋值
        topic.pub_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if request.files:
            f = request.files['picture']
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            ext=f.filename.split('.')[-1]
            filename=ftime+'.'+ext
            topic.images='upload/'+filename
            basedir=os.path.dirname(os.path.dirname(__file__))
            print(basedir)
            upload_path=os.path.join(basedir,'static/upload',filename)
            f.save(upload_path)
        db.session.add(topic)
        return redirect('/')

@main.route('/about')
def about_views():
    categories = Category.query.all()
    # 判断是否有登录的用户
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template('about.html',params=locals())

@main.route('/list')
def list_views():
    id = request.args['id']
    # print(id)
    categories = Category.query.all()
    # for cate in categories:
    #     print(cate.cate_name)
    topics = Topic.query.filter_by(category_id=id)
    # 判断是否有登录的用户
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template('list.html',params=locals())

@main.route('/photo')
def photo_views():
    categories = Category.query.all()
    for a in categories:
        print(a.cate_name)
    # 判断是否有登录的用户
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template('photo.html',params=locals())

@main.route('/time')
def time_views():
    categories = Category.query.all()
    # 判断是否有登录的用户
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template('time.html',params=locals())


@main.route('/gbook')
def gbook_views():
    categories = Category.query.all()
    # 判断是否有登录的用户
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template('gbook.html',params=locals())

@main.route('/info')
def info_views():
    categories = Category.query.all()
    for a in categories:
        print(a.cate_name)
    # 判断是否有登录的用户
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template('info.html',params=locals())

@main.route('/header')
def footer_views():
    return render_template('header.html')
