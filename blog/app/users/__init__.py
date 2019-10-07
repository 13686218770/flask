"""users包处理与用户相关的业务逻辑包(注册,登录,登出)"""

from flask import Blueprint

users = Blueprint('users',__name__)
from . import views