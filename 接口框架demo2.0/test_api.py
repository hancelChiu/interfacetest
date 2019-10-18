# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2019/10/14

import flask
import json
from flask import request

#创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
#@server.route()可以将普通函数转变为服务，登录接口的路径、请求方式
@server.route('/login', methods=['GET', 'POST'])
def login():
	data = []
	def get_data():
		if request.method == 'GET':
			#获取通过url请求传参的数据
			username = request.values.get('name')
			data.append(username)
			#获取URL请求传的密码，明文
			pwd = request.values.get('pwd')
			data.append(pwd)
		elif request.method == 'POST':
			#post获取表单中的参数
			username = request.form.get('name')
			data.append(username)
			pwd = request.form.get('pwd')
			data.append(pwd)
		return data
	data = get_data()
	print(data)

	#判断用户名、密码都不为空
	if data[0] and data[1]:
		if data[0] == 'xiaoming' and data[1] == '111':
			resu = {'code': 200, 'message': '登录成功'}
			return json.dumps(resu, ensure_ascii=False)#将字典转换为json字符串
		else:
			resu = {'code': -1, 'message': '账号密码错误'}
			return json.dumps(resu, ensure_ascii=False)
	else:
		resu = {'code': 10001, 'message':'参数不能为空!'}
		return json.dumps(resu, ensure_ascii=False)

if __name__ == '__main__':
	server.run(debug=True, port=8889, host='127.0.0.1')
