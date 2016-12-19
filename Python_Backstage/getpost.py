# coding=utf-8
from flask import Flask,request
import json 
app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        array = ['北京','上海']
	dic = {}
	dic['data'] = array
	print '===get==='
	return json.dumps(dic)
    else:
    	print '===post==='
    	dic = {}
    	if request.form['data'] == 'fuzongjian':
    		dic['data'] = 'Hello Fuzongjian'
    		return json.dumps(dic)
    	else:
    		dic['data'] = 'Hello World'
    		return json.dumps(dic)
if __name__ == '__main__':
    app.run(debug = True,host = '0.0.0.0',port = 2016)
