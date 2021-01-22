'''
Code description：test report
Create time：
Developer：
'''
from config import Conf
import os
from common.my_log import Log
import time
import logging
from package.HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport
import unittest
log = Log(__name__,file=logging.INFO,cmd=logging.INFO)
# 用HTMLTestRunner 实现的测试报告
def create_report():
    """

    :return:
    """
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = Conf.testreport + r'\report' + now + '.html'  #测试报告文件
    try:
        fp = open(fileName, 'wb')     #打开测试报告文件将结果写入其中
    except Exception:
        log.csp_log.exception('[%s] open error cause Failed to generate test report' % fileName)
    else:
        runner = HTMLTestRunner(stream=fp, title='中国电信5g消息运营商管理平台自动化测试报告',
             description='python3+selenium3+unittest+PO+excel')
        log.csp_log.info('successed to generate test report [%s]' % fileName)
        return runner, fp, fileName


def addcase(case_path=Conf.testcase, rule='test*.py'):
    """

    :param TCpath: 测试用例存放路径
    :param rule: 匹配的测试用例文件
    :return:  测试套件
    """
    discover = unittest.defaultTestLoader.discover(case_path,rule)

    return discover


# 用BeautifulReport模块实现测试报告
def runTc(discover):
    """

    :param discover: 测试套件
    :return:
    """
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = now + '.html'
    try:
        result = BeautifulReport(discover)
        result.report(filename=fileName, description='中国电信5g消息运营商管理平台自动化测试报告',report_dir=Conf.testreport)
    except Exception:
        log.csp_log.exception('Failed to generate test report', exc_info=True)
    else:
        log.csp_log.info('successed to generate test report [%s]' % fileName)
        return fileName


def Latest_report(report_dir=os.path.join(Conf.testreport)):
    """
    返回最新的测试报告文件
    :param report_dir:
    :return:
    """
    # os.listdir()方法用于返回指定文件夹包含文件或文件名字列表
    lists = os.listdir(report_dir)
    # 按照时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    file = os.path.join(report_dir, lists[-1])
    return file












if __name__ == '__main__':
    create_report()
    suite = addcase(rule='*TC.py')
    runTc(suite)