# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2019/10/14

import os
import logging
from logging.handlers import TimedRotatingFileHandler
import sys
sys.path.append('../')
import getpathInfo
from datetime import datetime

proDir = getpathInfo.get_Path()
resultPath = os.path.join(proDir, 'result')
log_path = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))  # 存放log文件的路径


class Logger(object):
	def __init__(self, logger_name='logs…'):
		if not os.path.exists(log_path):
			os.mkdir(log_path)
		self.logger = logging.getLogger(logger_name)
		logging.root.setLevel(logging.NOTSET)
		self.log_file_name = 'logs'  # 日志文件的名称
		self.backup_count = 5  # 最多存放日志的数量
		# 日志输出级别
		self.console_output_level = 'WARNING'
		self.file_output_level = 'DEBUG'
		# 日志输出格式
		self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	def get_logger(self):
		"""在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
		if not self.logger.handlers:  # 避免重复日志
			console_handler = logging.StreamHandler()
			console_handler.setFormatter(self.formatter)
			console_handler.setLevel(self.console_output_level)
			self.logger.addHandler(console_handler)

			# 每天重新创建一个日志文件，最多保留backup_count份
			file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, self.log_file_name), when='D',
			                                        interval=1, backupCount=self.backup_count, delay=True,
			                                        encoding='utf-8')
			file_handler.setFormatter(self.formatter)
			file_handler.setLevel(self.file_output_level)
			self.logger.addHandler(file_handler)
		return self.logger


logger = Logger().get_logger()