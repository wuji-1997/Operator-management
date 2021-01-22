# -- coding: utf-8 --

import logging
from selenium import webdriver
from common.my_log import Log

driver_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

class Driver(object):


    def chormedriver(self):
        """
        连接chorme驱动
        :return:
        """
        try:
            self.driver = webdriver.Chrome()

        except Exception:
            driver_log.csp_log.exception(f'connection {self.driver} FAIL,sorry  please install Chorme driver ')
            raise
        else:
            return self.driver

    def Firefoxdriver(self):
        """
        连接firefox驱动
        :return:
        """
        try:
            self.driver = webdriver.Firefox()

        except Exception:
            driver_log.csp_log.exception(f'connection {self.driver} FAIL,sorry  please install Firefox driver ')
            raise
        else:
            return self.driver

    def Iedriver(self):
        """
        连接chorme驱动
        :return:
        """
        try:
            self.driver = webdriver.Ie()

        except Exception:
            driver_log.csp_log.exception(f'connection {self.driver} FAIL,sorry  please install Ie driver ')
            raise
        else:
            return self.driver

if __name__=="__main__":
    test = Driver()
    value = test.chormedriver()
    print(value)

