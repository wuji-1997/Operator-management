import unittest
from webUI.config.Conf import *
from webUI.common import newreport
import time
from webUI.package.HTMLTestRunner import HTMLTestRunner
from webUI.common.sendemail import sendSmptEmail
#定义测试目录为当前目录


def all_case():
    """

    :return:
    """
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
    print(discover)
    return discover







'''
discover（）方法会自动根据测试目录test_dir 匹配查找测试用例文件，并将查找到的测试用例组装到测试套件中，因此，可以直接通过
run()方法执行discover，大大简化了测试用例的查找与执行
'''

if __name__=="__main__":

    runner = unittest.TextTestRunner()
    runner.run(all_case())

