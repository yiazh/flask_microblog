'''
Created on:

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
import os
class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'