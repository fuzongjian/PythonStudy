#coding:utf
from flask import Flask
import os
app = Flask(__name__)
#读
@app.route('/read',methods =['GET'])
def readFile():
	f = open('Python_Backstage/resource/fuzongjian.txt','r')
	# content = f.read()#读取全部内容
	content = f.read(100)#读取前100个字节
	print content,type(f),type(content),len(content)
	f.close()
	return content
#写
@app.route('/write')
def writeFile():
	content = '''电子科技大学清水河校区主楼工程位于四川省成都市高新技术开发区西区，是四川省高等学府电子科技大学标志性建筑，体量大，综合性强，功能性强，科技含量高，具有庄重、典雅的建筑风格，充分展现了现代高校的文化底蕴。
	'''
	new_file = 'Python_Backstage/resource/test.txt'
	f = open(new_file,'w')# 如果没有new_file这个文件，则会自动创建
	f.write(content)
	f.close()
	# os.system('touch %s' % new_file)  创建一个新的文件
	# os.mkdir('resource/test')   创建目录
	return 'fuzongjian'
if __name__ == '__main__':
	app.run(debug = True,host = '0.0.0.0',port = 2016)