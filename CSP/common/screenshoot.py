# -- coding: utf-8 --

from common.my_log import Log
from config import Conf

import logging
import time


screenshoot_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)



def screen_shoot(driver,dir,name):
    """
    截图
    :param driver: 浏览器驱动
    :param dir: 截图存放地址
    :param name: 截图名称
    :return:
    """
    now = time.strftime('%Y-%m-%d-%H-%M-%S')

    file =Conf.test_screenshoot+dir+r'\photo' +now +name+'.png'
    screenshoot_log.csp_log.info(f'screenshoot {name} save in {file} success')
    return driver.get_screenshot_as_file(file)







