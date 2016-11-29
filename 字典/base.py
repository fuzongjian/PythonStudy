#coding:utf-8
#创建和使用字典
def first():
	phonebook = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
	print phonebook,phonebook['Alice']
#dict函数通过其他映射或者键值对的序列建立字典
def second():
	items = [('name','Gumby'),('age',42)]
	d = dict(items)
	print d['name'],'\n',d
	dic = dict(name = 'fuzongjian',age = 42)
	print dic
#基本字典操作
'''
len(dict)返回dict中项（键-值对）的数量
del dict[k]删除键为k的项
k in dict 检查d中是否含有键为k的项 
'''
def third():
	people = {

		'Alice':{
			'phone':'1234',
			'addr':'Foo drive 23'
		},
		'Beth':{
			'phone':'2364',
			'addr':'Foo drive 23'
		},
		'Cecil':{
			'phone':'2345',
			'addr':'Foo drive 23'
		}
	}
	print len(people)
#字典的格式化字符串
def firth():
	template = '''
	<html>
		<head><title>%(title)s</title></head>
		<body>
			<h1>%(title)s</h1>
			<p>%(text)s</p>
		</body>
	</html>
	'''
	data = {'title':'My Home Page','text':'Welcome to my home page!'}
	print template % data
#字典方法
from copy import deepcopy
def fifth():
	#clear方法清除字典中的所有想。
	dic = {}
	dic['name'] = 'fuzongjian'
	print dic,'-----',dic.clear(),'-----',dic
	#copy方法返回一个具有相同键值对的新字典-----浅复制
	print '浅复制'
	x = {'name':'fuzongjian','age':['1','2','3']}
	y = x.copy()
	print x,'---',y
	y['name'] = 'fuzongyang'
	y['age'].remove('1')
	print x,'---',y
	#deepcopy深复制
	print '深复制'
	d = {}
	d['name'] = ['fuzongjian','fuzongyang']
	c = d.copy()
	dc = deepcopy(d)
	d['name'].append('fuzonglin')
	print c,'---',dc

	print 'fromkeys方法使用给定的键建立新的字典，每个键都对应一个默认的值None'
	print {}.fromkeys(['name','age'])
	print dict.fromkeys(['name','age'])
	print dict.fromkeys(['name','age'],'(unknown)')

	print 'get方法是个更宽松的访问字典项的方法'
	'''
	当我们使用dict[key]时，如果key不存在的话，一般会报错，而选择dict.get(key)不会报错，会返回一个None，同时自己也可自定义
	一个“默认值”，替换None
	'''
	test = {}
	print test.get('name')
	print test.get('name','fuzongjian')

	#has_key方法可以检查字典中是否含有特定的键
	sy = {'name':'fuzongjian'}
	print sy.has_key('age'),'---',sy.has_key('name')
	#items和iteritems
	#items方法将字典所有的项以列表的方式返回，列表中的每一项都标示为键值对的形式，但是项在返回时并没有遵循特定的次序
	wx = {'name':'fuzongjian','age':20,'hobby':'running'}
	print wx.items()
	#iteritems方法的作用大致相同，但是返回一个迭代器对象而不是列表
	print wx.iteritems(),'---',list(wx.iteritems())
	#key和iterkeys  ----values和itervalues
	#key方法将字典中的键以列表形式返回，而iterkeys则返回针对键的迭代器
	print wx.keys(),'---',wx.iterkeys(),'---',list(wx.iterkeys())
	print wx.values(),'---',wx.itervalues(),'---',list(wx.itervalues())
	#pop方法用来获取对应于给定键的值，然后将这个键-值对从字典中移除
	nb = {'name':'fuzongjian','hobby':'running'}
	print nb.pop('hobby'),'---',nb

	#popitem方法类似于list.pop,后者会弹出列表的最后一个元素，popitem弹出随机的项，因为字典元素随机
	ue = {'name':'fuzongjian','hobby':'running','age':1993}
	print ue.popitem()

	#setdefault方法在某种程度上类似于get方法，能够获得与给定键相关联的值，
	#除此之外，setdefault还能在字典这个不含有给定键的情况下设定相应的键值
	xn = {}
	print xn.setdefault('name','fuzongjian')
	xn['name'] = 'rabbit'
	print xn.setdefault('name','1234')
	print xn
	print xn.setdefault('age')

	#update方法可以利用一个字典更新另外一个字典
	vr = {'name':'fuzongjian'}
	ar = {'age':1993}
	vr.update(ar)
	print vr
def  appRun():
	fifth()
	# firth()
	# third()
	# second()
	# first()
if __name__ == '__main__':
	appRun()