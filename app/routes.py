'''
Created on:

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''

from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello world'
