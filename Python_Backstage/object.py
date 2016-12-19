# -*- coding:utf-8 -*-
class Employee(object):
	# 所有员工的基类
	empCount = 0 # 通过Employee.empCount来访问
	"""docstring for Employee"""
	def __init__(self, name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	def displayCount(self):
		print 'Total Employee %d' % Employee.empCount
		pass
	def displayEmployee(self):
		print 'Name:',self.name,'Salary:',self.salary
		pass
# 访问对象和属性
def objectAndAttr():
	object1 = Employee('fuzongjian',100000)#创建对象
	object1.displayCount()#调用对象方法
	object1.displayEmployee()

	# 添加、删除、修改类的属性
	object1.age = 25 #添加属性
	object1.age = 26 #修改属性
	print object1.age
	del object1.age #删除属性
	# print object1.age

	# 使用下面函数来访问属性
	print hasattr(object1,'salary')# 如果存在‘salary'属性返回True
	print getattr(object1, 'salary') # 返回‘salary’属性的值
	setattr(object1,'age',30)# 设置一个属性，如果属性不存在，会创建一个新的属性
	print object1.age
	delattr(object1,'age')# 删除属性
	pass
#Python 内置类属性
def selfAttr():
	print '类的文档字符串---Employee.__doc__:',Employee.__doc__
	print '类名---Employee.__name__',Employee.__name__
	'类定义所在的模块（类的全名是‘__main__.className’,如果类位于一个导入模块mymod中，那么className.__module__等于mymod）'
	print 'Employee.__module__',Employee.__module__
	'类的所有父类构成元素（包含了一个由所有父类组成的元组）'
	print 'Employee.__bases__',Employee.__bases__
	'''
	类的属性（包含一个字典，由类的数据属性组成）
	'''
	print 'Employee.__dict__',Employee.__dict__
	pass
if __name__ == '__main__':
	# objectAndAttr()
	# selfAttr()	


