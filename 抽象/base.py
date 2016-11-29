#coding:utf-8
#自定义斐波那契数列函数
def  fibs(num):
	result = [0,1]
	for i in range(num-2):
		result.append(result[-2]+result[-1])
	return result
def first():
	print fibs(10),fibs(num = 5)

#参数	
def test(str = 'fuzongjian'):
	print str
def second():
	test()
	test('fuzonglin')


#练习使用参数''
def story(**kwds):
	return 'Once upon a time,there was a %(job)s called %(name)s.' % kwds
def third():
	print story(job = 'King',name = 'Gumby')
	dic = {'job':'teacher','name':'Andy'}
	print story(**dic)
def appRun():
	third()
	# second()
	# first()
if __name__ == '__main__':
	appRun()