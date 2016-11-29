#coding:utf-8
def first():
	# 继承
	class A(object):
			def hello(self):
				print 'hello I\'m A'
			def  world(self):
				print 'hello world'
	class B(A):
		def hello(self):
			print 'hello I\'m B'
		pass
	b = B()
	b.hello()
	a = A()
	a.hello()
	a.world()
		
				
					
	pass
def appRun():
	first()
if __name__ == '__main__':
	appRun()