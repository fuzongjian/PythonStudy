# -*- coding:utf-8
import thread
import time
# 为线程定义一个函数
def print_time(threadName,delay):
	count = 0
	while count < 10:
		time.sleep(delay)
		count += 1
		print '%s:%s' % (threadName,time.ctime(time.time()))
		pass
	pass
def firstThread():
	try:
		thread.start_new_thread(print_time("Thread-1",2))
		thread.start_new_thread(print_time('thread-2',4))
	except:
		print 'Error: unable to start thread'
	while 1:
		pass

if __name__ == '__main__':
	firstThread()