import os
from webUI.config import Conf
from webUI.common.my_log import Log
import logging
screenshoot_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)
import time



def screen_shoot(driver,photo_name):
    """

    :param driver:浏览器驱动
    :param photo_name: 截图名称
    :return:
    """
    file_path  = Conf.photo_path +time.strftime('%Y-%m-%d')+'_'+photo_name+'.png'
    return driver.get_screenshot_as_file(file_path)

if __name__=="__main__":
    from selenium import webdriver
    import time
    broswer = webdriver.Chrome()
    broswer.get('http://isp.ct5g.cn/maap_isp/index')
    time.sleep(10)
    screen_shoot(driver=broswer,photo_name='first')
    broswer.quit()