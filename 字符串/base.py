#coding:utf-8
from math import pi
#字符串格式化：精简版
def first():
	print 'Hello,%s' % 'World'
	format = 'Hello,%s,%s'
	values = ('World','fuzongjian')
	print format % values

	format = 'pi with three decimals: %.3f'
	print format % pi
#模板字符串 
from string import Template
def second():
	#替换
	s = Template('$x,glorious $x!')
	print s.substitute(x='slurm')

	#替换单词中的某个部分 {}
	y = Template("It's ${x}tastic!")
	print y.substitute(x='slurm')

	#插入美元符号  $$
	z = Template('Make $$ selling $x')
	print z.substitute(x='slurm')

	#使用字典变量提供值/名称对
	w = Template('A $thing must never $action')
	dic = {}
	dic['thing'] = 'gentleman'
	dic['action'] = 'show his socks'
	print w.substitute(dic)
#字符串格式化完整版
def third():
	#简单转换
	print 'Price of eggs:$%d' % 42
	print 'Price of eggs:$%x' % 42
	print 'Pi: %f...' % pi
	print 'Very inexact estimate of pi: %i' % pi#带符号的十进制
	print 'Using str : %s' % 42L#使用repr转换成任意Python对象
	print 'Using str ：%r' % 42L#使用str转换成任意Python对象
	#字段宽度与精度
	print '%10f' % pi#输出十位，不够直接空格显示
	print '%10.2f' % pi
	print '%.2f' % pi
	print '%.5s' % 'Guido van Tossum'
	print '%.*s' % (5,'Guido van Tossum')#使用*作为字段宽度或者精度，此时数组会从元组参数中读出
	# 符号、对齐和用0填充
	print '%010.2f' % pi
	print '%-10.2f' % pi#使用（-）用来左对齐数值
	print ('%+5d' % 10) + '\n' + ('%+5d' % -10)#使用（+）表示不管是正数还是负数都标示出符号
#字符串方法
from string import maketrans
def firth():
	#find方法可以在一个较长的字符串中查找子串，它返回子串所在位置的最左端索引，如果没有找到则返回-1
	title = 'good good study'
	print title.find('study')
	print 'day day up'.find('up')
	subobject = '$$$ Get rich now!!! $$$'
	print subobject.find('$$$',1)#只提供起点
	print subobject.find('!!!',0,16)#提供起点和结束点

	#join方法是split方法的逆方法，用来连接序列中的元素
	sep = '+'
	seq = ['1','2','3','4']
	print sep.join(seq)
	dirs = '','usr','bin','env'
	print '/'.join(dirs)
	print 'C:'+'\\'.join(dirs)

	#split方法将字符串分割成序列
	print '1+2+3+4+5'.split('+')
	print '/usr/bin/env'.split('/')

	#lower方法返回字符串的小写字母版
	print 'Good good study'.lower()

	#replace方法返回某个字符串的所有匹配项均被替换之后得到字符串
	print 'fu zong jian'.replace('jian','yang')

	#strip方法返回去除两侧（不包括内部）空字符串（可以检测用户输入是否包含空字符串）
	print '     fuozngjian  '.strip()
	print '*** fu * zong * jian ***!!!'.strip('*!')#只会去掉两侧的字符

	#translate方法和replace方法一样，可以替换字符串中的某些部分，但是和前者不同的是，
	#translate方法只处理单个字符。他的优势在于可以同时进行多个替换，有些时候比replace效率高的多。
	table = maketrans('cs','kz')# c替换s，s替换z
	print 'this is an incredible test'.translate(table)
	print 'this is an incredible test'.translate(table,' ')#第二个参数可选，用来指定需要删除的字符

	print maketrans('','')[97:123]

	pass
def appRun():
	firth()
	# third()
	# second()
	# first()
if __name__ == '__main__':
	appRun()