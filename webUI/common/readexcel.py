#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'wuji'

from webUI.common.my_log import Log

import logging

from webUI.config.Conf import *
import xlrd

readexcel_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)


class ReadExcel(object):

    def __init__(self,filepath =None,sheet_name=None):
        """

        :param filepath:
        :param sheet_name:
        """
        try:
            self.workbook = xlrd.open_workbook(filepath)
            self.worksheet = self.workbook.sheet_by_name(sheet_name)
        except Exception:
            readexcel_log.action_log.exception(f'打开EXCEL文件{self.workbook}失败')
            raise
        else:
            readexcel_log.action_log.info(f'打开EXCEL文件{self.workbook}成功')

    def getexcelvalue(self,rows,cows):
        """

        :param rows:
        :param cows:
        :return:
        """
        try:
            value = self.worksheet.cell_value(rows,cows)
        except Exception:
            readexcel_log.action_log.exception(f'从EXCEL文件中获取值{value}失败')
            raise
        else:
            readexcel_log.action_log.info(f'从EXCEL文件中获取值"{value}"成功')
            return value
if __name__=="__main__":
    test= ReadExcel(filepath=excel_path+r'\test_iwebsns.xlsx',sheet_name='login')
    value = test.getexcelvalue(0,0)
    print(value)


