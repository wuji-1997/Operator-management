from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *
from Page.login_page import LoginPage_CSP
from common.readini import Readini
import os

update_pws_log = Log(__name__, file=logging.INFO, cmd=logging.INFO)

update_pws_date = ReadExcel(filepath=test_data + r'\test_update_password.xlsx', sheetname="update_pws")


class UpdatepwsPage(BasePage):


    updatedate=[(update_pws_date.get_excel(1,3),update_pws_date.get_excel(1,4)),   #0点击忘记密码按钮
                (update_pws_date.get_excel(2,3),update_pws_date.get_excel(2,4),update_pws_date.get_excel(2,5)),  #1找回密码-输入手机号
                (update_pws_date.get_excel(3,3),update_pws_date.get_excel(3,4)),   #2找回密码-点击获取验证码
                (update_pws_date.get_excel(4,3),update_pws_date.get_excel(4,4),update_pws_date.get_excel(4,5)),  #3找回密码-输入新密码
                (update_pws_date.get_excel(5,3),update_pws_date.get_excel(5,4)),  #4找回密码-再次输入新密码
                (update_pws_date.get_excel(6,3),update_pws_date.get_excel(6,4)),   #5点击确定按钮
                update_pws_date.get_excel(7,5), #原密码
                ]

    url =Readini().get_value(os.path.join(current_path,'config.ini'),'test_url','url3')

    def update_pws(self):
        """
        更新密码
        :return:
        """
        self.click_element(self.updatedate[0][0],self.updatedate[0][1])
        self.wait(2)
        self.input_value(self.updatedate[1][0],self.updatedate[1][1],self.updatedate[1][2])
        self.wait(2)
        self.click_element(self.updatedate[2][0],self.updatedate[2][1])
        self.wait(40)
        self.input_value(self.updatedate[3][0],self.updatedate[3][1],self.updatedate[3][2])
        self.wait(2)
        self.input_value(self.updatedate[4][0],self.updatedate[4][1],self.updatedate[3][2])
        self.wait(2)
        self.click_element(self.updatedate[5][0],self.updatedate[5][1])
        self.wait(2)
        self.F5()

    def new_login(self):
        """
        使用新密码登录
        :return:
        """
        login_date = LoginPage_CSP()
        login_date.user(pws=self.updatedate[3][2])
        login_date.clickphoto()
        login_date.clickmsg()
        login_date.loginbutton()
        self.wait(2)



