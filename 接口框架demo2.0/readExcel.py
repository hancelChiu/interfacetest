# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2019/10/14

import os
from xlrd import open_workbook
import getpathInfo

proDir = getpathInfo.get_Path()

# print(proDir)


class readExcel():
	# 从Excel文件中读取测试用例
	def get_xls(self, xls_name, sheet_name):
		cls = []
		#get xls file's path
		xlsPath = os.path.join(proDir, "testFile", 'case', xls_name)
		#open xls file
		file = open_workbook(xlsPath)
		#get sheet by name
		sheet = file.sheet_by_name(sheet_name)
		#get one sheet's rows
		nrows = sheet.nrows

		for i in range(nrows):
			if sheet.row_values(i)[0] != 'case_name':
				cls.append(sheet.row_values(i))
		return cls

if __name__ == '__main__':
	print(readExcel().get_xls('userCase.xlsx', 'test'))
	print(readExcel().get_xls('userCase.xlsx', 'test')[0][1])
	print(readExcel().get_xls('userCase.xlsx', 'test')[1][2])