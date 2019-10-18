# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2019/10/14


import requests
import json


class RunMain():

	#定义一个方法，传入需要的参数url和data
	def send_post(self, url, data):
		result = requests.post(url, data=data).json()
		res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
		return res

	def send_get(self, url, data):
		result = requests.get(url=url, params=data).json()
		res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
		return res

	def run_main(self, method, url=None, data=None):
		result = None
		if method == 'post':
			result = self.send_post(url, data)
		elif method == 'get':
			result = self.send_get(url, data)
		else:
			print('method值错误！！')
		return result

# if __name__ == '__main__':
# 	data = {
# 		"name": "xiaoming",
# 		"pwd": "111",
# 	}
# 	result = RunMain().run_main('post', 'http://127.0.0.1:8889/login', data)
# 	print(result)

