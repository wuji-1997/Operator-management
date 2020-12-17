from webUI.common.my_log import Log
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

base_log=Log(__name__,logging.INFO,cmd=logging.INFO)
class BasePage(object):


    def __init__(self,driver,url):
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
        self.base_url.maximize_window()
        self.base_url.implicitly_wait(10)

    def open(self):
        """

        :return:
        """
        try:
            self.__open(self.base_url)
        except Exception:
            base_log.action_log.exception(f'open url"{self.base_url}" fail !')
            raise
        else:
            base_log.action_log.info(f'open url"{self.base_url}" success !')

    def findelement(self,find_way,value):
        """

        :param find_way:
        :return:
        """
        if find_way=="id":
            element=(By.ID,value)
            try:
                WebDriverWait(driver=self.base_driver,timeout=10,poll_frequency=0.5).until(EC.invisibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')

        elif find_way=='name':
            element = (By.NAME, value)
            try:
                WebDriverWait(driver=self.base_driver, timeout=10, poll_frequency=0.5).until(
                    EC.invisibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')

        elif find_way=='class':
            element = (By.CLASS_NAME, value)
            try:
                WebDriverWait(driver=self.base_driver, timeout=10, poll_frequency=0.5).until(
                    EC.invisibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')

        elif find_way=='xpath':
            element = (By.XPATH, value)
            try:
                WebDriverWait(driver=self.base_driver, timeout=10, poll_frequency=0.5).until(
                    EC.invisibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')

        elif find_way=='link_text':
            element = (By.LINK_TEXT, value)
            try:
                WebDriverWait(driver=self.base_driver, timeout=10, poll_frequency=0.5).until(
                    EC.invisibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')

        elif find_way=='css':
            element = (By.CSS_SELECTOR, value)
            try:
                WebDriverWait(driver=self.base_driver, timeout=10, poll_frequency=0.5).until(
                    EC.invisibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')

        else:
            base_log.action_log.error(f'输入的定位方式值  {find_way}  有误')

    def input_value(self,find_way,value):
        """

        :param find_way:
        :param value:
        :return:
        """
        element = self.findelement(find_way,value)
        try:
            element.send_keys(value)
        except Exception:
            base_log.action_log.exception(f"输入值  {value} 失败")
            raise
        else:
            base_log.action_log.info(f"输入值  {value} 成功")

    def handle_select(self,find_way,value):
        """

        :param value:
        :return:
        """
        element = self.findelement(find_way,value)
        try:
            Select(element).select_by_visible_text(value)

        except Exception:
            base_log.action_log.exception(f'处理下拉框--{element}--- 失败')
            raise
        else:
            base_log.action_log.info(f'处理下拉框--{element}--- 成功')









if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
