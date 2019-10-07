"""main包为业务逻辑包
    包含与主题相关的所有的业务逻辑处理(发表,查看,删除,修改)
    通过蓝图(blueprint)将自己与app关联一起
"""
from  flask import Blueprint
#声明好蓝图之后,main就拥有与app相同的角色
main = Blueprint('main',__name__)
from . import views