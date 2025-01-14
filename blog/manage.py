"""启动和管理相关程序"""
from app import create_app,db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = create_app()#创建app对象
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()


