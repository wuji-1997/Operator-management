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
            except Exception as e:
                base_log.csp_log.exception(f'finding element timeout!,details',exc_info=True)
                raise e
            else:
                base_log.csp_log.info(f'The page of {self} had already find the element {element}')
                return self.base_driver.find_element(*element)

        elif find_way=='name':
            element = (By.NAME, value)
            try:
                WebDriverWait(self.base_driver, 10, 0.5).until(EC.visibility_of_element_located(element))
            except Exception as e:
                base_log.csp_log.exception(f'finding element timeout!,details', exc_info=True)
                raise e
            else:
                base_log.csp_log.info(f'The page of {self} had already find the element {element}')
                return self.base_driver.find_element(*element)

        elif find_way=='class':
            element = (By.CLASS_NAME, value)
            try:
                WebDriverWait(self.base_driver, 10, 0.5).until(EC.visibility_of_element_located(element))
            except Exception as e:
                base_log.csp_log.exception(f'finding element timeout!,details', exc_info=True)
                raise e
            else:
                base_log.csp_log.info(f'The page of {self} had already find the element {element}')
                return self.base_driver.find_element(*element)

        elif find_way=='xpath':
            element = (By.XPATH, value)
            try:
                WebDriverWait(self.base_driver, 10, 0.5).until(EC.visibility_of_element_located(element))
            except Exception as e:
                base_log.csp_log.exception(f'finding element timeout!,details', exc_info=True)
                raise e
            else:
                base_log.csp_log.info(f'The page of {self} had already find the element {element}')
                return self.base_driver.find_element(*element)

        elif find_way=='link_text':
            element = (By.LINK_TEXT, value)
            try:
                WebDriverWait(self.base_driver, 10, 0.5).until(EC.visibility_of_element_located(element))
            except Exception as e:
                base_log.csp_log.exception(f'finding element timeout!,details', exc_info=True)
                raise e
            else:
                base_log.csp_log.info(f'The page of {self} had already find the element {element}')
                return self.base_driver.find_element(*element)

        elif find_way=='css':
            element = (By.CSS_SELECTOR, value)
            try:
                WebDriverWait(self.base_driver, 10, 0.5).until(EC.visibility_of_element_located(element))
            except Exception as e:
                base_log.csp_log.exception(f'finding element timeout!,details', exc_info=True)
                raise e
            else:
                base_log.csp_log.info(f'The page of {self} had already find the element {element}')
                return self.base_driver.find_element(*element)

        else:
            base_log.csp_log.error(f'find_way  {find_way}  mistakened')

    def input_value(self,find_way,value,test_value):
        """
        定位元素后输入值
        :param find_way: 定位方式
        :param value:    元素表达式
        :param test_value: 文本框输入值
        :return:
        """
        inputB=self.findelement(find_way, value)
        try:
            inputB.send_keys(test_value)
        except Exception as e:
            base_log.csp_log.exception(f'typing value error!',exc_info=True)
            raise e
        else:
            base_log.csp_log.info(f'inputvalue:{value} is receiveing {test_value}')



    def click_element(self,find_way,value):
        """
        定位元素成功后点击元素
        :param find_way:
        :param value:
        :param number
        :return:
        """
        clickC=self.findelement(find_way,value)
        try:
            clickC.click()
        except Exception as e:
            base_log.csp_log.exception(f'click element error!', exc_info=True)
            raise e
        else:
            base_log.csp_log.info(f'click success success !')





    def handle_select(self,find_way,value,text):
        """
        处理下拉框
        :param value:
        :return:
        """
        selectB = self.findelement(find_way,value)
        try:
            Select(selectB).select_by_visible_text(text)

        except Exception as e:
            base_log.csp_log.exception(f'select handle error',exc_info=True)
            raise e
        else:
            base_log.csp_log.info(f'select_text:{value} is receiveing value:{text} ')

    def handleform(self,id):
        """
        内置表单处理
        :param value:
        :return:
        """

        try:
            self.base_driver.switch_to.frame(id)

        except Exception as e:
            base_log.csp_log.exception(f'id is not None')
            raise e
        else:
            base_log.csp_log.info(f'swith frame: {id} successed')

    def parentform(self):
        """
        返回上一层表单
        :return:
        """
        try:
            self.base_driver.switch_to.parent_frame()

        except Exception as e:
            base_log.csp_log.exception(f'back to the previous level Failed')
            raise e
        else:
            base_log.csp_log.info('back to the previous level successed')

    def defaultform(self):
        """
        返回最外层表单
        :return:
        """
        try:
            self.base_driver.switch_to.default_content()

        except Exception as e:
            base_log.csp_log.exception('reture outermost layer Failed')
            raise e
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

        try:
            element = self.base_driver.switch_to.alert
        except Exception:
            base_log.csp_log.exception(f'handle alert Failed',exc_info=True)
            raise
        else:
            base_log.csp_log.info(f'handle alert " {element} " successed')
            element.accept()


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
        except Exception as e:
            base_log.csp_log.exception(f'handle jsp:[{value}] Failed',exc_info=True)
            raise e
        else:
            base_log.csp_log.info(f'handle jsp:[{value}] successed')



    def get_text(self,find_way,elementvalue):
        """
        获取元素文本值
        :param find_way:
        :param value:
        :return:
        """
        element = self.findelement(find_way, elementvalue)
        try:
            value=element.text
        except Exception as e:
            base_log.csp_log.exception(f'{element} gets text value failed',exc_info=True)
            raise e
        else:
            base_log.csp_log.info(f'{element} gets text value successed')
            return value

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


        except Exception as e:
            base_log.csp_log.exception(f'upload attachment:{filepath} failed',exc_info=True)
            raise e
        else:
            base_log.csp_log.info(f'upload attachment:{filepath} successed')


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


    def isElementExist(self,element):
        """
        判断元素是否存在
        :param value:
        :return:
        """
        try:
            element=WebDriverWait(self.base_driver,10,0.5).until(EC.visibility_of_element_located(element))
            element.click()
        except Exception:
            base_log.csp_log.exception(f'{element} is non-existent',exc_info=True)
            return False
        else:
            base_log.csp_log.info(f'{element} is existent')
            return True


    def goback(self):
        """
        返回上一步
        :return:
        """
        self.base_driver.back()

    def over(self):
        """
        断开驱动
        :return:
        """
        self.base_driver.quit()



if __name__=="__main__":
    from selenium import webdriver























































