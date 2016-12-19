# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def QQemail():
	_user = "752410703@qq.com"
	_pwd  = "asnumhubgmolbeha"# 授权码 （开启POP3/SMTP服务（发件人））
	_to   = ["2917066078@qq.com"]

	#发送内容 text类型
	# msg = MIMEText("Test",'plain','utf-8')

	#发送链接
	mail_msg = '''
	<p> Python 邮件发送测试...</p>
	<p><a href='http://www.baidu.com'>http://www.baidu.com</a></p>

	'''
	msg = MIMEText(mail_msg,'html','utf-8')




	# 邮件主题
	msg["Subject"] = "测试发送邮件"
	# 发送人
	msg["From"]    = _user
	# 收件人
	msg["To"]      = ";".join(_to)

	try:
	    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
	    s.login(_user, _pwd)
	    s.sendmail(_user, _to, msg.as_string())
	    s.quit()
	    print "Success!"
	except smtplib.SMTPException,e:
	    print "Falied,%s"%e

# 带附件的邮件
def QQemailFile():
	_user = "752410703@qq.com"
	_pwd  = "asnumhubgmolbeha"# 授权码 （开启POP3/SMTP服务（发件人））
	_to   = ["2917066078@qq.com"]


    #创建一个带附件的实例
	message = MIMEMultipart()
	#邮件的正文
	message.attach(MIMEText("带附件的邮件",'plain','utf-8'))
	#构造附件
	att = MIMEText(open('Python_Backstage/material/file.txt','rb').read(),'base64','utf-8')
	att['Content-Type'] = 'application/octet-stream'
	#这里的filename可以任意写，写什么名字，邮件中显示什么名字
	att['Content-Disposition'] = 'attachment;filename=\'file.txt\''
	message.attach(att)

	# 邮件主题
	message["Subject"] = "测试发送邮件"
	# 发送人
	message["From"]    = _user
	# 收件人
	message["To"]      = ";".join(_to)

	try:
	    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
	    s.login(_user, _pwd)
	    s.sendmail(_user, _to, message.as_string())
	    s.quit()
	    print "Success!"
	except smtplib.SMTPException,e:
	    print "Falied,%s"%e
	pass
if __name__ == '__main__':
	# QQemail()
	QQemailFile()
	