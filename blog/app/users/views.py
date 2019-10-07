"""与用户相关的路由和视图"""
from . import users
from ..models import *
from flask import render_template,request,make_response,session,redirect
import re

@users.route('/login',methods=['GET','POST'])
def users_views():
    if request.method == 'GET':
        resp = make_response(render_template('login.html'))
        # 获取请求源地址保存进cookies
        url = request.headers.get('Referer','/')
        resp.set_cookie('url',url)
        return resp
    else:
        #1.接收提交过来的用户名和密码
        username = request.form['username']
        password = request.form['password']
        #2.验证用户名和密码的有效性
        user = User.query.filter_by(loginname=username,upwd=password).first()
        #3.给出响应
        if user:
            #1.登录成功保存进session
            session['id']=user.ID
            session['loginname']=user.loginname
            #2.从哪里来回哪里去(从cookie中获取请求源地址)
            url = request.cookies.get('url')
            return redirect(url)
        else:
            emsg="用户名或密码错误"
            return render_template('login.html',emsg=emsg)


@users.route('/register',methods=['GET','POST'])
def register_views():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        email = request.form['email']
        url = request.form['url']
        password = request.form['password']
        password1 = request.form['password1']
        # print('username:',username)
        # print(email,url,password,password1)
        user = User.query.filter_by(loginname=username).first()
        if user:
            return render_template('register.html',username=username,email=email,url=url,emsg="该用户已存在")
        elif re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            if password != password1:
                emsg = '两次密码输入不一致，请重新输入'
                return render_template('register.html',username=username,email=email,url=url,emsg = emsg)
            user=User()
            user.loginname=username
            user.email=email
            user.url=url
            user.uname=username
            user.upwd=password
            db.session.add(user)
            db.session.commit()
            # topics = Topic.query.limit(10).all()
            # categories = Category.query.all()
            # return render_template('index.html',params=locals())
            return render_template('login.html',username=username)
        return render_template('register.html', username=username, email=email, url=url, emsg="邮箱格式不正确")

@users.route('/logout')
def logout_views():
    #获取请求源地址
    url = request.headers.get('Referer','/')
    #判断session中是否有登录信息,如果有则删除
    if 'id' in session and 'loginname' in session:
        del session['id']
        del session['loginname']
    #重定向到源地址
    return redirect(url)

