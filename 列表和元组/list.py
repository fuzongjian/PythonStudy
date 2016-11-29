#coding:utf-8

# 切片
def first():
	print '切片'
	numbers = [1,2,3,4,5,6,7,8,9,0]
	print numbers[3:6]	
	print numbers[-3:-1]
	print numbers[:3]
	print numbers[-3:]
	print numbers[0:10:2]
	print numbers[::4]#

# 序列相加 只有相同类型的序列才可以进行连接操作
def second():
	print '系列相加'
	print [1,2,3] + [4,5,6]
	print 'Hello ' + 'world'

# 乘法  用数字X乘以一个序列会生成新的序列，而在新的序列中，原来的序列将被重复X此
def third():
	print '乘法'
	print 'fuzongjian' * 2
	print [1,2] * 3
	print '空列表初始化'
	print [None] * 10

#成员资格
def firth():
	print 'f' in 'fuzongjian'
	database = [
		['alert','1234'],
		['fuzongjian','7890']
	]
	username = raw_input('User name:')
	pin = raw_input('PIN code:')
	print [username,pin] in database
#长度、最小值和最大值
def fifth():
	nums = [12,14,9,23,15]
	print len(nums)
	print max(nums)
	print min(nums)
def appRun():
	fifth()
	first()
	second()
	third()
	firth()
if __name__ == '__main__':
	appRun()