#coding:utf-8
def first():
	nu = 1,2,3
	print nu
	se = 2
	print se
	ye = 2,
	print ye
def second():
	print 'tuple函数的功能和list函数基本上是一样的：以一个序列作为参数并把它转换为元组'
	print tuple([1,2,3])
	print tuple('abc')
	print tuple((1,2,3))
def appRun():
	second()
	# first()
if __name__ == '__main__':
	appRun()