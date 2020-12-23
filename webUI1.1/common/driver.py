from selenium import webdriver
from webUI.common.my_log import Log
import logging

driver_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

class Getdriver(object):


    def usechorme(self):

        try:
            self.driver =webdriver.Chrome()
        except Exception:
            driver_log.action_log.exception('请先安装chorme驱动')
            raise
        else:
            driver_log.action_log.info(f'启动{self.driver}驱动成功')
            return self.driver

    def useie(self):
        """

        :return:
        """
        try:
            self.driver =webdriver.Ie()
        except Exception:
            driver_log.action_log.exception('请先安装IE驱动')
            raise
        else:
            driver_log.action_log.info(f'启动{self.driver}驱动成功')
            return self.driver

    def use_firefox(self):
        """

        :return:
        """
        try:
            self.driver =webdriver.Firefox()
        except Exception:
            driver_log.action_log.exception('请先安装chorme驱动')
            raise
        else:
            driver_log.action_log.info(f'启动{self.driver}驱动成功')
            return self.driver
if __name__=="__main__":
    test = Getdriver()
    testone = test.usechorme()
    testone.get_screenshot_as_file()
