# -*- coding:utf-8 -*-
import json
def first():
	dict_str = '{"name":"fuzongjian"}'
	print type(dict_str)
	# print json.loads(dict_str)
	dict_json = json.loads(dict_str)
	print type(dict_json),dict_json
	pass
if __name__ == '__main__':
	first()
