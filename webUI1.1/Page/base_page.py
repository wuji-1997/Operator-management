from webUI.common.my_log import Log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

base_log=Log(__name__,logging.INFO,cmd=logging.INFO)

class BasePage(object):




    def __init__(self,driver,url='http://localhost/iwebsns/index.php'):
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

        base_log.action_log.info(f'open url"{self.base_url}" success !')

    def findelement(self,find_way,value):
        """
        查询单个元素
        :param find_way:
        :return:
        """
        if find_way=="id":
            element=(By.ID,value)
            try:
                WebDriverWait(self.base_driver,10,1).until(EC.visibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')
                return self.base_driver.find_element(*element)

        elif find_way=='name':
            element = (By.NAME, value)
            try:
                WebDriverWait(self.base_driver,10,1).until(EC.visibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')
                return self.base_driver.find_element(*element)

        elif find_way=='class':
            element = (By.CLASS_NAME, value)
            try:
                WebDriverWait(driver=self.base_driver, timeout=10, poll_frequency=0.5).until(
                    EC.visibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')
                return self.base_driver.find_element(*element)

        elif find_way=='xpath':
            element = (By.XPATH, value)
            try:
                WebDriverWait(driver=self.base_driver, timeout=10, poll_frequency=0.5).until(
                    EC.visibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')
                return self.base_driver.find_element(*element)

        elif find_way=='link_text':
            element = (By.LINK_TEXT, value)
            try:
                WebDriverWait(driver=self.base_driver, timeout=10, poll_frequency=0.5).until(
                    EC.visibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')
                return self.base_driver.find_element(*element)

        elif find_way=='css':
            element = (By.CSS_SELECTOR, value)
            try:
                WebDriverWait(driver=self.base_driver, timeout=10, poll_frequency=0.5).until(
                    EC.visibility_of_element_located(element))
            except Exception:
                base_log.action_log.exception(f'定位元素{element}失败')
                raise
            else:
                base_log.action_log.info(f'定位元素{element}成功')
                return self.base_driver.find_element(*element)

        else:
            base_log.action_log.error(f'输入的定位方式值  {find_way}  有误')

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
            base_log.action_log.exception(f"输入值  {test_value} 失败")
            raise
        else:
            base_log.action_log.info(f"输入值  {test_value} 成功")

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
            base_log.action_log.exception(f"点击元素失败")
            raise
        else:
            base_log.action_log.info(f"点击元素成功")


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
            base_log.action_log.exception(f'处理下拉框--{element}--- 失败')
            raise
        else:
            base_log.action_log.info(f'处理下拉框--{element}--- 成功')

    def handleform(self,id):
        """
        内置表单处理
        :param value:
        :return:
        """

        try:
            self.base_driver.switch_to.frame(id)

        except Exception:
            base_log.action_log.exception(f'切换表单失败')
            raise
        else:
            base_log.action_log.info('切换表单成功')

    def parentform(self):
        """
        返回上一层表单
        :return:
        """
        try:
            self.base_driver.switch_to.parent_frame()

        except Exception:
            base_log.action_log.exception(f'返回上一层表单失败')
            raise
        else:
            base_log.action_log.info('返回上一层表单成功')

    def defaultform(self):
        """
        返回最外层表单
        :return:
        """
        try:
            self.base_driver.switch_to.default_content()

        except Exception:
            base_log.action_log.exception(f'返回最外层表单失败')
            raise
        else:
            base_log.action_log.info('返回最外层表单成功')


    def get_title(self):
        """
        获取当前页面标题
        :return:
        """
        value = self.base_url.title
        base_log.action_log.info(f"获取当前页面标题为{value}")
        return value

    def get_url(self):
        """
        获取当前页面的网址
        :return:
        """
        now_url = self.base_driver.current_url
        base_log.action_log.info(f'获取页面网址{now_url}')
        return now_url

    def getpagecode(self):
        """
        获取页面的源码
        :return:
        """
        value = self.base_driver.page_source
        base_log.action_log.info('获取当前页面源码成功')
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
            base_log.action_log.exception(f'清空元素输入框失败')
            raise
        else:
            base_log.action_log.info(f'清空元素输入框成功')

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
            base_log.action_log.exception(f"处理提示框{element}失败")
            raise
        else:
            base_log.action_log.info(f"处理提示框{element}成功")


if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()

    driver.switch_to.default_content()
    driver.find_element().clear()
























