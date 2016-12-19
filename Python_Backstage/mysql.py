#-*- coding:utf-8 -*-
from flask import Flask
import json
app = Flask(__name__)
import MySQLdb

# 增删改
@app.route('/update')
def update():
	#二、通过制定参数（ip、用户名、密码、数据库）连接到某个数据库
	db = MySQLdb.connect(host = 'localhost',user = 'root',passwd = 'deltalpha',db ='fuzongjian',charset = 'utf8')
	cursor = db.cursor()
	# sql = 'update fullstack set name = \'baiqiuen\' where name = \'zhouenlai\''  #更新
	# sql = 'insert into fullstack(id,name,age)values(6,\'fuzongmiao\',26)'     #  增
	sql = 'delete from fullstack where name = \'fuzongyang\''   # 删

	try:
		#执行sql语句
		cursor.execute(sql)
		#提交到数据库
		db.commit()
	except:
		#发生错误回滚
		db.rollback()
	db.close()
	return 'state'
#查询
@app.route('/query')
def query():
	#二、通过制定参数（ip、用户名、密码、数据库）连接到某个数据库
	db = MySQLdb.connect(host = 'localhost',user = 'root',passwd = 'deltalpha',db ='fuzongjian',charset = 'utf8')
	#三、使用cursor()方法获取操作游标
	cursor = db.cursor()
	#四、行为要执行的SQL语句，这句是创建一个名为main的表
	# sql = "select * from mafengwojingdian limit " + str((int(page)-1)*7) + ','+ str(7)
	insertSql = 'insert into fullstack(id,name,age)values(4,\'fuzongyang\',26)'
	searchsql = 'select * from fullstack'
	#五、执行SQL语句
	cursor.execute(insertSql)
	db.commit()
	cursor.execute(searchsql)
	result = cursor.fetchall()
	db.close()
	print type(result),result[0][0],len(result)
	json_dic = {}
	json_array = []
	for obj in result:
		json_array.append(dealobj(obj))
	json_dic['data'] = json_array
	json_dic['status'] = str(1);
	print type(result)
	return json.dumps(json_dic)
	# return 'hello'
def dealobj(obj):
	dic = {}
	dic['name'] = obj[1]
	dic['age'] = str(obj[2])
	return dic
if __name__ == '__main__':
	app.run(host = '0.0.0.0',port = 2016,debug = True)