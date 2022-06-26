'''
Created on:

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models