#!/usr/bin/python
#coding:utf-8
def first():
	for i in range(1,5):
		for j in range(1,5):
			for k in range(1,5):
				if (i != k) and (i != j) and (j != k):
					print 'i = ' + str(i) + 'j = ' + str(j) + 'k = ' + str(k)
def second():
	i = int(raw_input('净利润：'))
	print i
	arr = [1000000,600000,400000,200000,100000,0]
	rat = [0.01,0.015,0.03,0.05,0.075,0.1]
	r = 0
	for idx in range(0,6):
		if i > arr[idx]:
			r += (i - arr[idx] * rat[idx])
			print (i-arr[idx])*rat[idx]
			i = arr[idx]
			print r
		pass
import math
def third():
	for i in range(10000):
		x = int(math.sqrt(i + 100))
		y = int(math.sqrt(i + 268))
		if (x * x == i + 100) and (y * y == i + 268):
			print i 
			pass
def firth():
	year = int(raw_input('year: \n'))
	month = int(raw_input('month:\n'))
	day = int(raw_input('day:\n'))
	months = (0,31,59,90,120,151,181,212,243,273,304,334)
	if 0 < month <= 12:
		sum 
		
		pass
def apprun():
	# first()
	# second()
	third()
	pass
if __name__ == '__main__':
	apprun()
