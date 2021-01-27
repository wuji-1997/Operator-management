from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *
from Page.login_page import LoginPage_CSP
from common.readini import Readini
import os
from selenium import webdriver

update_pws_log = Log(__name__, file=logging.INFO, cmd=logging.INFO)

update_pws_date = ReadExcel(filepath=test_data + r'\test_update_password.xlsx', sheetname="update_pws")


class UpdatepwsPage(BasePage):


    updatedate=[(update_pws_date.get_excel(1,3),update_pws_date.get_excel(1,4)),   #0点击忘记密码按钮
                (update_pws_date.get_excel(2,3),update_pws_date.get_excel(2,4),update_pws_date.get_excel(2,5)),  #1找回密码-输入手机号
                (update_pws_date.get_excel(3,3),update_pws_date.get_excel(3,4)),   #2找回密码-点击获取验证码
                (update_pws_date.get_excel(4,3),update_pws_date.get_excel(4,4),update_pws_date.get_excel(4,5)),  #3找回密码-输入新密码
                (update_pws_date.get_excel(5,3),update_pws_date.get_excel(5,4)),  #4找回密码-再次输入新密码
                (update_pws_date.get_excel(6,3),update_pws_date.get_excel(6,4)),   #5点击确定按钮
                update_pws_date.get_excel(7,5), #6原密码
                (update_pws_date.get_excel(8,3),update_pws_date.get_excel(8,4),update_pws_date.get_excel(8,5)),  #7输入账号
                (update_pws_date.get_excel(9,3),update_pws_date.get_excel(9,4)),  #8输入新密码
                (update_pws_date.get_excel(10,3),update_pws_date.get_excel(10,4)), #9点击图片验证码
                (update_pws_date.get_excel(11,3),update_pws_date.get_excel(11,4)), #10短信验证码
                (update_pws_date.get_excel(12,3),update_pws_date.get_excel(12,4)), #11点击登录按钮
                (update_pws_date.get_excel(13,3),update_pws_date.get_excel(13,4)), #12
                (update_pws_date.get_excel(14,3),update_pws_date.get_excel(14,4)), #13
                ]

    url =Readini().get_value(os.path.join(current_path,'config.ini'),'test_url','url3')

    def update_pws(self,pws):
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
        self.input_value(self.updatedate[3][0],self.updatedate[3][1],pws)
        self.wait(2)
        update_pws_log.csp_log.info(f'输入新密码-----{pws}')
        self.input_value(self.updatedate[4][0],self.updatedate[4][1],pws)
        update_pws_log.csp_log.info(f'再次输入新密码-----{pws}')
        self.wait(2)
        self.click_element(self.updatedate[5][0],self.updatedate[5][1])
        self.wait(2)
        self.F5()


    def new_login(self,latest_pws):
        """
        使用新密码登录
        :param latest_pws: 最新的密码
        :return:
        """
        self.input_value(self.updatedate[7][0],self.updatedate[7][1],self.updatedate[7][2])
        self.wait(2)
        self.input_value(self.updatedate[8][0],self.updatedate[8][1],latest_pws) #输入新密码
        self.wait(2)
        self.click_element(self.updatedate[9][0],self.updatedate[9][1])   #点击图片验证码
        self.wait(20)
        self.click_element(self.updatedate[10][0],self.updatedate[10][1]) #短信验证码
        self.wait(40)
        self.click_element(self.updatedate[11][0],self.updatedate[11][1]) #点击登录按钮
        self.wait(6)

    def login_out(self):
        """
        推出登录
        :return:
        """
        self.click_element(self.updatedate[12][0],self.updatedate[12][1])
        self.wait(2)
        self.click_element(self.updatedate[13][0],self.updatedate[13][1])
        self.wait(5)






