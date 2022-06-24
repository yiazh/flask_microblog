'''
Created on:

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes