# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2019/10/15


import json
import unittest
import sys
sys.path.append('../')
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel

url = geturlParams.geturlParams().get_url()
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'test')


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
	def setParameters(self, case_name, path, query, method):
		self.case_name = str(case_name)
		self.path = str(path)
		self.query = str(query)
		self.method = str(method)

	def description(self):
		return self.case_name

	def setUp(self):
		print(self.case_name + '测试开始前准备')

	def test01case(self):
		self.checkResult()

	def tearDown(self):
		print('测试结束，输出log完结\n')

	#断言
	def checkResult(self):
		url1 = 'http://www.xxx.com/login?'#url格式需要注意
		new_url = url1 + self.query
		data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
		info = RunMain().run_main(self.method, url, data1)
		info_dic = json.loads(info)
		print(info_dic)
		if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
			self.assertEqual(info_dic['code'], 200)
			print('登录成功')
		if self.case_name == 'login_error':  # 同上
			self.assertEqual(info_dic['code'], -1)
		if self.case_name == 'login_null':  # 同上
			self.assertEqual(info_dic['code'], 10001)

if __name__ == '__main__':
	testUserLogin().checkResult()