# -- coding: utf-8 --

import xlrd
import logging
from config.Conf import *
from common.my_log import Log

readexcel_log = Log(__name__,file=logging.INFO,cmd=logging.WARN)

class ReadExcel(object):

    def __init__(self,filepath,sheetname):
        """

        :param filepath:数据地址
        :param sheetname: sheet页名称
        """
        self.filepath =filepath
        self.workbook = xlrd.open_workbook(filepath)
        self.worksheet_name = self.workbook.sheet_by_name(sheetname)


    def get_excel(self,rows,cloxs):
        """

        :return:
        """

        try:
            value = self.worksheet_name.cell_value(rows,cloxs)

        except Exception:
            readexcel_log.csp_log.exception(f'from {self.filepath} get value-- failed')
            raise
        else:
            readexcel_log.csp_log.info(f'from {self.filepath} get value-- "{value}"-- successed')
            return value





if __name__=="__main__":
    test = ReadExcel(filepath=test_data+r'\add_csp.xlsx',sheetname='CSP信息申请模板')

    value = test.get_excel(2,1)
    print(value)



