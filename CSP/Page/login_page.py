from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *
from common.readini import Readini


csplogin_log=Log(__name__,file=logging.INFO,cmd=logging.INFO)
csplogin_excel=ReadExcel(filepath=test_data+r'\test_login_data.xlsx',sheetname="login")


class LoginPage_CSP(BasePage):

    username = [(csplogin_excel.get_excel(1,3),csplogin_excel.get_excel(1,4),csplogin_excel.get_excel(1,5)),
                csplogin_excel.get_excel(2,5), #错误的账号
                (csplogin_excel.get_excel(3,3),csplogin_excel.get_excel(3,4),csplogin_excel.get_excel(3,5)),
                csplogin_excel.get_excel(4,3), #输入错误的密码
                (csplogin_excel.get_excel(5,3),csplogin_excel.get_excel(5,4))]  #登录按钮

    photo = (csplogin_excel.get_excel(6,3),csplogin_excel.get_excel(6,4))
    msg = (csplogin_excel.get_excel(7,3),csplogin_excel.get_excel(7,4))


    def loginbutton(self):
        """
        登录按钮
        :return:
        """
        self.click_element(self.username[4][0],self.username[4][1])

    def user(self,email="wuji2020",pws='.WKE$gpJGr5H'):
        """
        输入账号与密码
        :param email:
        :param pws:
        :return:
        """
        self.input_value(self.username[0][0],self.username[0][1],email)
        self.wait(1)
        self.input_value(self.username[2][0],self.username[2][1],pws)
        self.wait(1)

    def clickphoto(self):
        """
        图形验证码
        :return:
        """
        self.click_element(self.photo[0], self.photo[1])
        self.wait(15)

    def clickmsg(self):
        """
        手机短信验证码
        :return:
        """
        self.click_element(self.msg[0], self.msg[1])
        self.wait(40)


    def csp_login(self):
        """
        统一登录
        :return:
        """
        self.open()
        self.user()
        self.clickphoto()
        self.clickmsg()
        self.loginbutton()





if __name__=="__main__":
    from selenium import webdriver
    from Page.csp_page import CspPage




    driver = webdriver.Chrome()
    test = LoginPage_CSP(driver)
    test.open()

    test.csp_login()

    add = CspPage(driver)
    add.test_add()

    test.upload_file('id','agentFront',r'E:\test\test_first.jpg')


    '''

    driver.find_element_by_id('agentFront').click()


    shell = win32com.client.Dispatch('WScript.shell')
    test.wait(5)
    shell.SendKeys(r'E:\test\test_first.jpg')
    test.wait(5)
    win32api.keybd_event(13, 0, 0, 0)  # (回车)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
    win32api.keybd_event(13, 0, 0, 0)  # (回车)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(2)

    test.wait(5)

    # SendKeys
    '''











