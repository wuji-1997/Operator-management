# -- coding: utf-8 --

import os
from common.readini import Readini
#当前所在路径
current_path = os.path.split(os.path.realpath(__file__))[0]

#项目路径
project = Readini().get_value(os.path.join(current_path,'config.ini'),'project','project_path')

#测试数据路径

test_data = os.path.join(project,'data')

#测试用例路径

testcase = os.path.join(project,'test_case')

#测试报告路径

testreport = os.path.join(project,'report')

#测试截图路径

test_screenshoot = os.path.join(project,'screenshoot','CSP')

#日志文件路径

log_path = os.path.join(project,'log','my_log')

#记事本路径

notebook = os.path.join(project,'data')
