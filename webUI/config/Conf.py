import os
from webUI.common.readini import Readini

#当前路径
current_path = os.path.split(os.path.realpath(__file__))[0]
#os.path.realpath(__file__)返回当前执行脚本的路径
#os.path.split()返回工作项目路径和当前执行脚本文件名以元组形式返回

read_path = Readini()
#项目路径:D:\webapp
projectpath =read_path.get_configvalue(os.path.join(current_path,'config.ini'),'project','project_path')

#log路径
#D:\webapp\webUI\LOG\log
log_path = os.path.join(projectpath,'webUI','LOG','log')

#测试数据文件路径
#D:\webapp\webUI\data\test_data.xlsx
excel_path =os.path.join(projectpath,'webUI','data','test_data.xlsx')

#测试用例路径
#D:\demo\webUI\test_case
case_path = os.path.join(projectpath,'webUI','test_case')

#测试截图路径
##D:\demo\webUI\report\screenshot
photo_path = os.path.join(projectpath,'webUI','report','screenshot','photo')


