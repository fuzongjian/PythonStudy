# -*- coding:utf-8 -*-
import re
def first():
	# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，就返回None
	print (re.match('www','www.baidu.com').span())#在起始位置匹配
	print (re.match('com','www.baidu.com'))#不在起始位置匹配
def second():
	line = 'Cats are smarter than dogs'
	matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
	if matchObj:
		print 'matchObj.group() : ',matchObj.group()
		print 'matchObj.group(1) : ',matchObj.group(1)
		print 'matchObj.group(2) : ',matchObj.group(2)
	else:
		print 'Nothing found'
	pass
def third():
	# re.search(),扫描整个字符串并返回第一个成功的匹配
	print (re.search('www','www.baidu.com').span())#在起始位置匹配
	print (re.search('com','www.baidu.com').span())#不在起始位置匹配
	pass
def forth():
	line = 'Cats are smarter than dogs'
	searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
	if searchObj:
		print 'searchObj.group() : ',searchObj.group()
		print 'searchObj.group(1) : ',searchObj.group(1)
		print 'searchObj.group(2) : ',searchObj.group(2)
	else:
		print 'Nothing found'
	pass
#re.match与re.search的区别
# re.match值匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，返回None
# re.search匹配整个字符串，直到找到一个匹配
def fifth():
	line = "Cats are smarter than dogs";

	matchObj = re.match( r'dogs', line, re.M|re.I)
	if matchObj:
   		print "match --> matchObj.group() : ", matchObj.group()
	else:
  		print "No match!!"

	matchObj = re.search( r'dogs', line, re.M|re.I)
	if matchObj:
   		print "search --> matchObj.group() : ", matchObj.group()
	else:
   		print "No match!!"
	pass

#检索和替换 
# re.sub(pattern, repl, string, count=0, flags=0)
# pattern : 正则中的模式字符串
# rel : 替换的字符串，也可以为一个函数
# string : 要被查找替换的原始字符串
# count : 模式匹配后替换的最大次数，默认0表示替换所有的匹配
def sixth():

	phone = '2004-959-559 #这是一个国外电话号码'
	#删除字符串中的 Python注释
	num = re.sub(r'#.*$','',phone)
	print '电话号码是：',num
	#删除非数字（-）的字符串
	num = re.sub(r'\D','',phone)
	print '电话号码是：',num

	#repl参数是一个函数
	s = 'A23G4HFD567'
	print(re.sub('(?P<value>\d+)',doubled,s))
	pass
	
def doubled(matched):
	value = int(matched.group('value'))
	return str(value*2)

if __name__ == '__main__':
	# first()
	# second()
	# third()
	# forth()
	# fifth()
	sixth()
	