#coding:utf-8
#list函数
def first():
	print list('fuzongjian')
#基本的列表操作
def second():
	numbers = [1,2,3,4,5]
	numbers[1] = 0
	print '改:',numbers
	del numbers[1]
	print '删:',numbers
	print '分片赋值'
	oldList = list('fuzongjian')
	oldList[6:] = list('yang')
	print oldList
#列表方法
def third():
	lst = [1,2,3]
	lst.append(4)
	print 'append方法用于列表末尾追加新的对象'
	print lst

	print 'count方法统计某个元素在列表中出现的次数'
	print ['good','good','study','day','day','up'].count('good')

	print 'extend方法可以在列表的末尾一次性直接另一个序列中的多个值'
	# extend 修改了a序列，而数列的相加则是放回新的列表
	a = [1,2,3]
	b = [4,5,6]
	c = [7,8,9]
	a.extend(b)
	print'a.extend(b) =',a,'\n','b + c = ',b + c,'\n','b = ',b,'c = ',c

	print 'index方法用于从列表中找出某个值第一个匹配项的索引位置'
	saying = ['good','good','study','day','day','up']
	print saying.index('day')

	print 'insert方法用于将对象插入到列表中'
	numbers = [1,2,3,4,5]
	numbers.insert(3,'four')
	print numbers

	print'pop方法会移除列表中的一个元素（默认最后一个），并且返回该元素值'
	poplist = [1,2,3]
	poplist.pop()
	print poplist
	poplist.pop(1)
	print poplist

	print 'remove方法用于移除列表中某个值得第一个匹配项'
	x = ['yes','good','saying','good']
	x.remove('good')
	print x

	print 'reverse方法将列表中的元素方向存放'
	y = ['fu','zong','jian']
	y.reverse()
	print y

	print 'sort方法用于原位置对列表进行排序'
	w = [2,3,1,7,8,4]
	w.sort()
	print w
#高级排序
def cmp(a,b):
	if a > b:
		return -1
	else:
		return 1
def advancedSort():
	xy = [13,2,3,23,56,34,23]
	xy.sort(cmp)
	print xy

	hlist = ['fu','zong','hai']
	hlist.sort(key=len)
	print hlist

	wx = [13,2,3,23,56,34,23]
	wx.sort(reverse = True)
	print wx
def appRun():
	advancedSort()
	# third()
	# second()
	# first()
if __name__ == '__main__':
	appRun()