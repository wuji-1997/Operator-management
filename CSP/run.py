'''
 Code description：auto run test case
 Create time：
 Developer：
 '''
import unittest
import time
from config.Conf import *
from common.newreport import create_report,addcase,runTc,Latest_report
from common import sendemail


'''
discover（）方法会自动根据测试目录test_dir 匹配查找测试用例文件，并将查找到的测试用例组装到测试套件中，因此，可以直接通过
run()方法执行discover，大大简化了测试用例的查找与执行
'''

if __name__ == "__main__":

    #test_suite = addcase()
    #filename = runTc(test_suite)
    send_report = Latest_report()
    sendemail.sendSmptEmail().send_email(send_report)
