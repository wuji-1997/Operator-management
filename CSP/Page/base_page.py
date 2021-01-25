from common.my_log import Log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import win32api
import win32con
import win32com.client
from config.Conf import *
import os
import random

base_log=Log(__name__,logging.INFO,cmd=logging.INFO)
read_config = Readini()
class BasePage(object):




    def __init__(self,driver,url=read_config.get_value(os.path.join(current_path,'config.ini'),'test_url','url1')):
        """

        :param driver:
        :param url:
        """
        self.base_driver= driver
        self.base_url = url

    def __open(self,test_url):
        """

        :param test_url:
        :return:
        """
        self.base_driver.get(test_url)
        self.base_driver.maximize_window()
        self.base_driver.implicitly_wait(10)


    def open(self):
        """
        打开浏览器
        :return:
        """

        self.__open(self.base_url)

        base_log.csp_log.info(f'open url"{self.base_url}" success !')

    def findelement(self,find_way,value):
        """
        查询单个元素
        :param find_way:
        :return:
        """
        if find_way=="id":
            element=(By.ID,value)
            try:
                WebDriverWait(self.base_driver,10,0.5).until(EC.visibility_of_element_located(element))
            except Exception:
                base_log.csp_log.exception(f'locate {element} Failed')
                raise
            else:
                base_log.csp_log.info(f'locate {element} successed')
                return self.base_driver.find_element(*element)

        elif find_way=='name':
            element = (By.NAME, value)
            try:
                WebDriverWait(self.base_driver,10,0.5).until(EC.visibility_of_element_located(element))
            except Exception:
                base_log.csp_log.exception(f'locate {element} Failed')
                raise
            else:
                base_log.csp_log.info(f'locate {element} successed')
                return self.base_driver.find_element(*element)

        elif find_way=='class':
            element = (By.CLASS_NAME, value)
            try:
                WebDriverWait(self.base_driver,10,0.5).until(EC.visibility_of_element_located(element))
            except Exception:
                base_log.csp_log.exception(f'locate {element} Failed')
                raise
            else:
                base_log.csp_log.info(f'locate {element} successed')
                return self.base_driver.find_element(*element)

        elif find_way=='xpath':
            element = (By.XPATH, value)
            try:
                WebDriverWait(self.base_driver,10,0.5).until(EC.visibility_of_element_located(element))
            except Exception:
                base_log.csp_log.exception(f'locate {element} Failed')
                raise
            else:
                base_log.csp_log.info(f'locate {element} successed')
                return self.base_driver.find_element(*element)

        elif find_way=='link_text':
            element = (By.LINK_TEXT, value)
            try:
                WebDriverWait(self.base_driver,10,0.5).until(EC.visibility_of_element_located(element))
            except Exception:
                base_log.csp_log.exception(f'locate {element} Failed')
                raise
            else:
                base_log.csp_log.info(f'locate {element} successed')
                return self.base_driver.find_element(*element)

        elif find_way=='css':
            element = (By.CSS_SELECTOR, value)
            try:
                WebDriverWait(self.base_driver,10,0.5).until(EC.visibility_of_element_located(element))
            except Exception:
                base_log.csp_log.exception(f'locate {element} Failed')
                raise
            else:
                base_log.csp_log.info(f'locate {element} successed')
                return self.base_driver.find_element(*element)

        else:
            base_log.csp_log.error(f'find_way  {find_way}  mistakened')

    def input_value(self,find_way,value,test_value):
        """

        :param find_way:
        :param value:
        :param test_value:
        :return:
        """

        try:
            self.findelement(find_way, value).send_keys(test_value)
        except Exception:
            base_log.csp_log.exception(f"input  {test_value} Failed")
            raise
        else:
            base_log.csp_log.info(f"input  {test_value} successed")

    def click_element(self,find_way,value):
        """
        点击元素
        :param find_way:
        :param value:
        :return:
        """
        element = self.findelement(find_way,value)
        try:
            element.click()
        except Exception:
            base_log.csp_log.exception(f"click {value} Failed")
            raise
        else:
            base_log.csp_log.info(f"click {value} successed")


    def handle_select(self,find_way,value,text):
        """
        处理下拉框
        :param value:
        :return:
        """
        element = self.findelement(find_way,value)
        try:
            Select(element).select_by_visible_text(text)

        except Exception:
            base_log.csp_log.exception(f'handle select--{value}--- Failed')
            raise
        else:
            base_log.csp_log.info(f'handle select--{value}--- successed')

    def handleform(self,id):
        """
        内置表单处理
        :param value:
        :return:
        """

        try:
            self.base_driver.switch_to.frame(id)

        except Exception:
            base_log.csp_log.exception(f'switch frame Failed')
            raise
        else:
            base_log.csp_log.info('swith frame successed')

    def parentform(self):
        """
        返回上一层表单
        :return:
        """
        try:
            self.base_driver.switch_to.parent_frame()

        except Exception:
            base_log.csp_log.exception(f'back to the previous level Failed')
            raise
        else:
            base_log.csp_log.info('back to the previous level successed')

    def defaultform(self):
        """
        返回最外层表单
        :return:
        """
        try:
            self.base_driver.switch_to.default_content()

        except Exception:
            base_log.csp_log.exception('reture outermost layer Failed')
            raise
        else:
            base_log.csp_log.info('reture outermost layer successed')


    def get_title(self):
        """
        获取当前页面标题
        :return:
        """
        value = self.base_url.title
        base_log.csp_log.info(f'get title is  " {value} "')
        return value

    def get_url(self):
        """
        获取当前页面的网址
        :return:
        """
        now_url = self.base_driver.current_url
        base_log.csp_log.info(f'get url is " {now_url} "')
        return now_url

    def getpagecode(self):
        """
        获取页面的源码
        :return:
        """
        value = self.base_driver.page_source
        base_log.csp_log.info('get page source code successed')
        return value

    def clear_input(self,find_way,value):
        """
        清空输入框
        :param find_way:
        :param value:
        :return:
        """
        element = self.findelement(find_way,value)

        try:
            element.clear()
        except Exception:
            base_log.csp_log.exception(f'clear input Failed')
            raise
        else:
            base_log.csp_log.info(f'clear input successed')

    def wait(self,value):
        """
        强制等待
        :param value:
        :return:
        """
        time.sleep(value)

    def handlealert(self):
        """
        处理ALERT类型提示框
        :return:
        """
        element = self.base_driver.switch_to.alert
        try:
            element.accept()

        except Exception:
            base_log.csp_log.exception(f'handle alert " {element} " Failed')
            raise
        else:
            base_log.csp_log.info(f'handle alert " {element} " successed')


    def handle_frame(self):
        """
        多窗口操作
        :return:
        """
        first_frame = self.base_driver.current_window_handle  #获取当前句柄
        all_frame =self.base_driver.window_handles            #获取所有打开的句柄
        self.wait(5)
        for test_frame in all_frame:
            if test_frame!=first_frame:
                base_log.csp_log.exception(f'open more frame failed')
            else:
                value=self.get_url()
                base_log.csp_log.info(f'open more frame successed get url is {value}')
                return value



    def frame_close(self):
        """
        关闭当前窗口
        :return:
        """
        self.base_driver.close()


    def jsp(self,value):
        """
        执行jsp脚本处理时间控件
        :param value:
        :return:
        """
        try:
            self.base_driver.execute_script(value)
        except Exception:
            base_log.csp_log.exception(f'handle jsp " {value} " Failed')
            raise
        else:
            base_log.csp_log.info(f'handle jsp " {value} " successed')



    def get_text(self,find_way,elementvalue):
        """
        获取元素文本值
        :param find_way:
        :param value:
        :return:
        """

        element=self.findelement(find_way,elementvalue)
        return element.text



    def display(self,find_way,value):
        """
        判断元素是否可见
        :param find_way:
        :param value:
        :return:
        """
        element  = self.findelement(find_way,value)
        if element.is_displayed():
            base_log.csp_log.info(f'element is displayed')
            element.click()
        else:
            base_log.csp_log.info(f'element is not displayed')


    def upload_file(self,findway,value,filepath):
        """
        非input标签文件上传
        :param find_way:
        :param value:
        :param filepath:
        :return:
        """
        element= self.findelement(findway,value)
        try:
            element.click()
            shell = win32com.client.Dispatch('WScript.shell')
            self.wait(4)
            shell.SendKeys(filepath)
            self.wait(4)
            win32api.keybd_event(13, 0, 0, 0)  # (回车)
            win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
            win32api.keybd_event(13, 0, 0, 0)  # (回车)
            win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


        except Exception:
            base_log.csp_log.exception(f'上传文件 failed')
            raise
        else:
            base_log.csp_log.info(f'上传文件 successed')


    def F5(self):
        """
        页面刷新
        :return:
        """
        self.base_driver.refresh()
        base_log.csp_log.info('页面刷新成功')

    def random_number(self):
        """
        生成随机整数
        :return:
        """
        code_list=[]

        for i in range(10):
            code_list.append(str(i))

        code=random.sample(code_list,6)
        value = ''.join(code)
        return value


    def isElementExist(self,findway,elementvalue):
        """
        判断元素是否存在
        :param value:
        :return:
        """
        flag = True

        try:
            self.findelement(findway,elementvalue).click()

        except Exception:
            base_log.csp_log.exception(f'元素存在但不可操作')
            flag = False
            return flag
        else:
            base_log.csp_log.info('元素存在且可以操作')
            return flag


    def goback(self):
        """
        返回上一步
        :return:
        """
        self.base_driver.back()





















if __name__=="__main__":
    value = '中国电信100010'
    value2 = value+'1'
    print(value2)
    from selenium import webdriver
    driver = webdriver.Chrome()
    v =driver.find_element().text

































