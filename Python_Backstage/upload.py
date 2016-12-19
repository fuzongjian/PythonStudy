from flask import Flask,request
from werkzeug import secure_filename
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'Python_Backstage/resource/'
app.config['ALLOWED_EXTENSIONS'] = set(['png','jpg','txt','jpeg','pdf','gif'])
@app.route('/')
def index():
	return 'Hello World'
@app.route('/upload',methods = ['POST'])
def upload():
	print '===POST==='
	# file = request.files.get('file')
	upload_file = request.files.get('file')
	print upload_file.filename
	if upload_file and allowed_file(upload_file.filename):
		filename = secure_filename(upload_file.filename)
		upload_file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		return 'hell'
		pass
	# print 'filename == ' + file.filename
	# if file and allowed_file(file.filename):
	# 	filename = secure_filename(file.filename)
	# 	file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
	# 	return 'yes'
def allowed_file(filename):
	return '.' in filename and  filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']
	pass
if __name__ == '__main__':
	app.run(debug = True,host = '0.0.0.0',port = 2016)
