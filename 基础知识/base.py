#coding:utf-8

#模块
import math
def first():
	print math.floor(32.9),math.ceil(32.9)
	print int(math.floor(45.2))

#from 模块 import 函数
from math import sqrt
def second():
	print sqrt(9)
# cmath和复数
import cmath
def third():
	print cmath.sqrt(-9)

def appRun():
	first()
	second()
	third()
if __name__ == '__main__':
	appRun()