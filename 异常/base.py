#coding:utf-8
def first():
	while True:
		try:
			x = input('Enter the first number:')
			y = input('Enter the second number:')
			value = x / y
			print 'x/y is',value
		except Exception, e:
			print 'Invalid input:',e
			print 'Please tyr again'
			raise
		else:
			break
			pass
		finally:
			pass
def appRun():
	first()
if __name__ == '__main__':
	appRun()