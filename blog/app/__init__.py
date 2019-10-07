"""app包含所有程序处理的相关文件(静态文件,模板文件,实体类以及各个业务包处理)"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#声明SQLALCHEMY的实例
db = SQLAlchemy()

def create_app():
    #创建flask程序实例
    app = Flask(__name__)
    #指定各种配置
    app.config['DEBUG']=True
    app.config['SECRET_KEY']='sfdgsdh45645'
    app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:123456@localhost:3306/blog"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    #关联db和app
    db.init_app(app)
    #将main蓝图程序与app相关联
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 将users蓝图程序与app相关联
    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    #返回flask程序实例
    return app


