from webUI.common.my_log import Log
import logging
from webUI.Page.base_page import BasePage
from webUI.common.readexcel import ReadExcel
from webUI.config.Conf import *


login_log=Log(__name__,file=logging.INFO,cmd=logging.INFO)
login_excel=ReadExcel(filepath=excel_path+r'\test_iwebsns.xlsx',sheet_name="login")

class LoginPage(BasePage):


    input_email=[login_excel.getexcelvalue(2,3),login_excel.getexcelvalue(2,4),login_excel.getexcelvalue(2,5)]  #输入正确的账户
    bademail = login_excel.getexcelvalue(3,5)

    input_pws=[login_excel.getexcelvalue(4,3),login_excel.getexcelvalue(4,4),login_excel.getexcelvalue(4,5)] #输入正确的密码
    badpassword = login_excel.getexcelvalue(5,5)

    loginbutton = (login_excel.getexcelvalue(6,3),login_excel.getexcelvalue(6,4))


    def login_button(self):
        """
        点击登录按钮
        :return:
        """
        self.click_element(self.loginbutton[0],self.loginbutton[1])
        login_log.action_log.info("---------------------------登录中------------------------------------")

    def cleer_email(self):
        """
        清空账号输入框
        :return:
        """
        self.clear_input(self.input_email[0],self.input_email[1])
        login_log.action_log.info(f'清空输入框{self.input_email[1]}成功')

    def clear_pws(self):
        """
        清空密码输入框
        :return:
        """
        self.clear_input(self.input_pws[0],self.input_pws[1])
        login_log.action_log.info(f'清空输入框{self.input_pws[1]}成功')

    def login(self,email="13382197195@189.cn",pws='wuji0121'):
        """
        统一登录
        :param email:
        :param pws:
        :return:
        """
        self.input_value(self.input_email[0],self.input_email[1],email)
        self.input_value(self.input_pws[0],self.input_pws[1],pws)
        self.login_button()
        login_log.action_log.info('登录成功')


if __name__=="__main__":
    pass













