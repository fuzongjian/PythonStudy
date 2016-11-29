#coding:utf-8
def first():
	#如果在结尾处加上逗号，那么接下来的语句会与前一条语句在同一行打印
	print 'Hello,',
	print 'World!'

import math as foobar
from math import sqrt as fobar
def second():
	#从模块导入函数的时候，可以使用下面的
	# import somemodule
	# import somemodule from somefunction 
	# import somemodule from somefunction,anotherfunction,yetanotherfunction
	# from somemodule import *

	#如果两个模块有相同的函数，则采用第一种方式导入，如函数名为open
	# module1.open()
	# module2.open()

	#为整个模块去个别名
	#import math as foobar
	print foobar.sqrt(4)
	#from math import sqrt as fobar
	print fobar(4)

def third():
	print '赋值魔法'
	print '1、序列解包'
	values = 1,2,3
	x,y,z = values
	print x,y,z
	print '相等运算符'
	# is运算符是判定同一性而不是相等性。
	x = y = [1,2,3]
	z = [1,2,3]
	print x == y,x == z
	print x is y,x is z
	print [1,2] < [2,1]
	print '迭代'
	for number in x:
		print number
	print range(0,10),range(9)
	for num in range(3):
		print num
	print '循环遍历字典元素'
	d = {'x':1,'y':2,'z':3}
	for key in d:
		print key,'corresponds to',d[key]
	for key,value in d.items():
		print key,'corresponds to',value
	print '迭代工具'
	print '并行迭代'
	names = ['yang','jian','lin','hai']
	ages = [12,34,23,20]
	for i in range(len(names)):
		print names[i],'is',ages[i],'years old'


	print 'zip函数，将两个序列压缩在一起，然后返回一个元组的列表'
	print zip(names,ages)
	for name,age in zip(names,ages):
		print name,'is',age,'years old'
	#zip函数可以作用于任意多的序列，可以处理不等长的序列，当最短的序列用完的时候就会停止
	print zip(range(5),xrange(1000))
	print "enumerate 函数"
	for index,numb in enumerate(['fu','zong','jian']):
		print index,numb
	print '列表推导式——轻量级循环'
	print [x*x for x in range(10)]
	print [x*x for x in range(10) if x % 3 == 0]
	print [(x,y) for x in range(3) for y in range(2)]

	girls = ['alice','bernice','clarice']
	boys = ['chris','arnold','bob']
	letterGirls = {}
	for girl in girls:
		letterGirls.setdefault(girl[0],[]).append(girl)
	print [b+'+'+g for b in boys for g in letterGirls[b[0]]]

	print 'del'
	# 删除的只是名称，而不是列表本身，事实上，在python中是没有办法删除值
	x = y = ['Hello','World']
	y[1] = 'python'
	print x
	del x 
	print y

	print '使用exec和eval执行和求值字符串'
	
	pass
def appRun():
	third()
	# second()
	# first()
if __name__ == '__main__':
	appRun()