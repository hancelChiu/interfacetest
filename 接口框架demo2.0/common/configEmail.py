# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2019/10/15

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
import sys
sys.path.append('../')
import readConfig as readConfig
sys.path.append('F:\Python\python接口自动化\接口框架demo2.0\common')
import Log as Log


localReadConfig = readConfig.ReadConfig()
log_path = Log.log_path
host = localReadConfig.get_email('mail_host')
user = localReadConfig.get_email('mail_user')
password = localReadConfig.get_email('mail_pass')
port = localReadConfig.get_email('mail_port')
sender = localReadConfig.get_email('sender')
title = localReadConfig.get_email('subject')
content = localReadConfig.get_email('content')
mail_path = os.path.join(log_path, "report.html")  # 获取测试报告路径
#defined email subject
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subject = title + "" + date
value = localReadConfig.get_email('receiver')
receiver = []
#get receiver list
for n in str(value).split(","):
	receiver.append(n)

class send_email():
	def send163(self):

		# 创建一个带附件的实例
		message = MIMEMultipart()
		message['From'] = sender
		message['To'] = ';'.join(receiver)
		message['Subject'] = Header(subject, 'utf-8')

		# 邮件正文内容
		message.attach(MIMEText(content, 'plain', 'utf-8'))
		att = MIMEText(open(mail_path, 'rb').read(), 'base64', 'utf-8')
		att["Content-Type"] = 'application/octet-stream'
		att["Content-Disposition"] = 'attachment; filename="report_test.html"'
		message.attach(att)
		smtp = smtplib.SMTP_SSL()  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
		smtp.connect(host)
		smtp.login(user, password)
		smtp.sendmail(sender, receiver, message.as_string())
		print("邮件发送成功！！！")
		smtp.quit()



if __name__ == '__main__':
	email = send_email()
	email.send163()






