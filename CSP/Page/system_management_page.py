from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *

system_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)


account_date=ReadExcel(filepath=test_data+r'\test_system_management.xlsx',sheetname="账号管理")
role_date =ReadExcel(filepath=test_data+r'\test_system_management.xlsx',sheetname="角色管理")
sensitive_date = ReadExcel(filepath=test_data+r'\test_system_management.xlsx',sheetname="敏感词库管理")

class SyStem_Management_Page(BasePage):


    accountdate=[(account_date.get_excel(1,3),account_date.get_excel(1,4)),    #0点击系统管理
                 (account_date.get_excel(2,3),account_date.get_excel(2,4)),   #1点击账号管理
                 (account_date.get_excel(3,3),account_date.get_excel(3,4)),  #2输入用户名
                 (account_date.get_excel(4,3),account_date.get_excel(4,4)),  #3输入用户姓名
                 (account_date.get_excel(5,3),account_date.get_excel(5,4)),  #4输入手机号
                 (account_date.get_excel(6,3),account_date.get_excel(6,4)),  #5选择所属角色
                 (account_date.get_excel(7,3),account_date.get_excel(7,4)),  #6选择角色状态
                 (account_date.get_excel(8,3),account_date.get_excel(8,4)),  #7点击查询按钮
                 (account_date.get_excel(9,3),account_date.get_excel(9,4)),  #8点击编辑按钮
                 (account_date.get_excel(10,3),account_date.get_excel(10,4),account_date.get_excel(10,5)),  #9变更用户名
                 (account_date.get_excel(11,3),account_date.get_excel(11,4),account_date.get_excel(11,5)),  #10点击确认变更按钮
                 (account_date.get_excel(12,3),account_date.get_excel(12,4)),  #11点击删除按钮
                 (account_date.get_excel(13,3),account_date.get_excel(13,4)),  #12点击停用按钮
                 (account_date.get_excel(14,3),account_date.get_excel(14,4)),  #13点击新增账号按钮
                 (account_date.get_excel(15,3),account_date.get_excel(15,4),account_date.get_excel(15,5)),  #14输入新增的用户名
                 (account_date.get_excel(16,3),account_date.get_excel(16,4),account_date.get_excel(16,5)),  #15输入新增的用户姓名
                 (account_date.get_excel(17,3),account_date.get_excel(17,4),account_date.get_excel(17,5)),  #16输入新增的身份证号
                 (account_date.get_excel(18,3),account_date.get_excel(18,4),account_date.get_excel(18,5)),  #17点击上传身份证正面
                 (account_date.get_excel(19,3),account_date.get_excel(19,4),account_date.get_excel(19,5)),  #18点击上传身份证反面
                 (account_date.get_excel(20,3),account_date.get_excel(20,4),account_date.get_excel(20,5)),  #19选择所属角色
                 (account_date.get_excel(21,3),account_date.get_excel(21,4),account_date.get_excel(21,5)),  #20选择所属区域
                 (account_date.get_excel(22,3),account_date.get_excel(22,4),account_date.get_excel(22,5)),  #21输入新增的手机号码
                 (account_date.get_excel(23,3),account_date.get_excel(23,4),account_date.get_excel(23,5)),  #22输入新增的邮箱
                 (account_date.get_excel(24,3),account_date.get_excel(24,4),account_date.get_excel(24,5)),  #23输入新增的密码
                 (account_date.get_excel(25,3),account_date.get_excel(25,4)),  #24点击确认新增按钮
                 ]

    roledate=[(role_date.get_excel(1,3),role_date.get_excel(1,4)),   #0点击角色管理
              (role_date.get_excel(2,3),role_date.get_excel(2,4)),   #1输入角色名称
              (role_date.get_excel(3,3),role_date.get_excel(3,4)),   #2点击查询按钮
              (role_date.get_excel(4,3),role_date.get_excel(4,4)),   #3点击编辑按钮
              (role_date.get_excel(5,3),role_date.get_excel(5,4),role_date.get_excel(5,5)), #4输入变更角色名称
              (role_date.get_excel(6,3),role_date.get_excel(6,4)),   #5点击确认变更按钮
              (role_date.get_excel(7,3),role_date.get_excel(7,4)),   #6点击删除按钮
              (role_date.get_excel(8,3),role_date.get_excel(8,4)),   #7点击复制按钮
              (role_date.get_excel(9,3),role_date.get_excel(9,4),role_date.get_excel(9,5)),  #8输入复制的角色名称
              (role_date.get_excel(10,3),role_date.get_excel(10,4)),  #9点击新增角色
              (role_date.get_excel(11,3),role_date.get_excel(11,4),role_date.get_excel(11,5)),  #10输入新增角色名称
              (role_date.get_excel(12,3),role_date.get_excel(12,4),role_date.get_excel(12,5)),  #11输入新增角色权限描述
              ]

    sensitivedate=[(sensitive_date.get_excel(1,3),sensitive_date.get_excel(1,4)),   #0点击敏感词库管理
                   (sensitive_date.get_excel(2,3),sensitive_date.get_excel(2,4)),   #1点击新增字词
                   (sensitive_date.get_excel(3,3),sensitive_date.get_excel(3,4),sensitive_date.get_excel(3,5)), #2输入敏感字词
                   (sensitive_date.get_excel(4,3),sensitive_date.get_excel(4,4)),  #3点击确认新增按钮
                   (sensitive_date.get_excel(5,3),sensitive_date.get_excel(5,4)),  #4输入关键字
                   (sensitive_date.get_excel(6,3),sensitive_date.get_excel(6,4)),  #5点击查询按钮
                   (sensitive_date.get_excel(7,3),sensitive_date.get_excel(7,4)),  #6点击编辑按钮
                   (sensitive_date.get_excel(8,3),sensitive_date.get_excel(8,4),sensitive_date.get_excel(8,5)), #7输入变更的敏感字词
                   (sensitive_date.get_excel(9,3),sensitive_date.get_excel(9,4)), #8点击确认变更按钮
                   (sensitive_date.get_excel(10,3),sensitive_date.get_excel(10,4)), #9点击删除按钮
                   ]


    def intouser(self):
        """
        进入账号管理二级菜单
        :return:
        """
        self.click_element(self.accountdate[0][0],self.accountdate[0][1])  #点击系统管理一级菜单
        system_log.csp_log.info(f'点击系统管理一级菜单')
        self.click_element(self.accountdate[1][0],self.accountdate[1][1])
        system_log.csp_log.info(f'点击账号管理二级菜单')
        self.handleform(0)
        system_log.csp_log.info(f'切换至账号管理内置表单')

    def find_user(self,username,usernumber,usertype,userstatus):
        """
        查询账号
        :param username:用户名
        :param usernumber:手机号
        :param usertype:所属角色
        :return:
        """
        self.input_value(self.accountdate[2][0],self.accountdate[2][1],username)
        system_log.csp_log.info(f'输入用户名----{username}')
        self.wait(2)
        self.input_value(self.accountdate[4][0], self.accountdate[4][1], usernumber)
        system_log.csp_log.info(f'输入手机号码----{usernumber}')
        self.wait(2)
        self.handle_select(self.accountdate[5][0], self.accountdate[5][1],usertype)
        system_log.csp_log.info(f'选择所属角色----{usertype}')
        self.wait(2)
        self.handle_select(self.accountdate[6][0],self.accountdate[6][1],userstatus)
        system_log.csp_log.info(f'选择状态为----{userstatus}')
        self.wait(2)
        self.click_element(self.accountdate[7][0],self.accountdate[7][1])
        system_log.csp_log.info(f'点击查询按钮')
        self.wait(2)

    def add_user(self):
        """
        新增一个账号
        :return:
        """
        self.intouser()
        self.click_element(self.accountdate[13][0],self.accountdate[13][1])
        system_log.csp_log.info('点击新增账号按钮')
        self.wait(2)
        self.input_value(self.accountdate[14][0],self.accountdate[14][1],self.accountdate[14][2])
        system_log.csp_log.info(f'输入新增的账号-用户名---{self.accountdate[14][2]}')
        self.wait(2)
        self.input_value(self.accountdate[15][0], self.accountdate[15][1], self.accountdate[15][2])
        system_log.csp_log.info(f'输入新增的账号-用户姓名---{self.accountdate[15][2]}')
        self.wait(2)
        self.input_value(self.accountdate[16][0], self.accountdate[16][1], self.accountdate[16][2])
        system_log.csp_log.info(f'输入新增的账号-身份证号---{self.accountdate[16][2]}')
        self.wait(2)
        self.upload_file(self.accountdate[17][0],self.accountdate[17][1],self.accountdate[17][2])
        system_log.csp_log.info(f'上传新增的账号-身份证正面---{self.accountdate[17][2]}')
        self.wait(2)
        self.upload_file(self.accountdate[18][0], self.accountdate[18][1], self.accountdate[18][2])
        system_log.csp_log.info(f'上传新增的账号-身份证反面---{self.accountdate[18][2]}')
        self.wait(2)
        self.input_value(self.accountdate[19][0], self.accountdate[19][1], self.accountdate[19][2])
        system_log.csp_log.info(f'选择新增的账号--所属角色--{self.accountdate[19][2]}')
        self.wait(2)
        self.input_value(self.accountdate[20][0], self.accountdate[20][1], self.accountdate[20][2])
        system_log.csp_log.info(f'输入新增的账号-所属区域---{self.accountdate[20][2]}')
        self.wait(2)
        self.input_value(self.accountdate[21][0], self.accountdate[21][1], self.accountdate[21][2])
        system_log.csp_log.info(f'输入新增的账号-手机号码---{self.accountdate[21][2]}')
        self.wait(2)
        self.input_value(self.accountdate[22][0], self.accountdate[22][1], self.accountdate[22][2])
        system_log.csp_log.info(f'输入新增的账号-联系邮箱---{self.accountdate[22][2]}')
        self.wait(2)
        self.input_value(self.accountdate[23][0], self.accountdate[23][1], self.accountdate[23][2])
        system_log.csp_log.info(f'输入新增的账号-密码---{self.accountdate[23][2]}')
        self.wait(2)
        self.click_element(self.accountdate[24][0],self.accountdate[24][1])
        system_log.csp_log.info(f'点击确认新增按钮')
        self.wait(2)
        self.F5()

    def detele_user(self):
        """
        删除账号
        :return:
        """
        self.click_element(self.accountdate[11][0],self.accountdate[11][1])
        system_log.csp_log.info(f'点击删除按钮')
        self.wait(2)

    def update_user(self):
        """
        变更账号
        :return:
        """
        self.click_element(self.accountdate[8][0],self.accountdate[8][1])
        system_log.csp_log.info(f'点击编辑按钮')
        self.clear_input(self.accountdate[9][0],self.accountdate[9][1])
        system_log.csp_log.info(f'清空用户名输入框')
        self.wait(2)
        self.input_value(self.accountdate[9][0],self.accountdate[9][1],self.accountdate[9][2])
        system_log.csp_log.info(f'变更账号用户名为----{self.accountdate[9][2]}')
        self.wait(2)
        self.input_value(self.accountdate[23][0], self.accountdate[23][1], self.accountdate[23][2])
        system_log.csp_log.info(f'输入密码---{self.accountdate[23][2]}')
        self.wait(2)
        self.click_element(self.accountdate[10][0],self.accountdate[10][1])
        system_log.csp_log.info(f'点击确认变更按钮')
        self.wait(2)
        self.F5()

    def stop_user(self):
        """
        停用账号
        :return:
        """
        self.click_element(self.accountdate[12][0],self.accountdate[12][1])
        system_log.csp_log.info(f'点击停用按钮')
        self.wait(2)



    def assert_text(self,text):
        """
        断言文本
        :param text:
        :return:
        """
        value  =f'<span>{text}</span>'
        return value

    def intorole(self):
        """
        进入角色管理
        :return:
        """
        self.click_element(self.accountdate[0][0], self.accountdate[0][1])  # 点击系统管理一级菜单
        system_log.csp_log.info(f'点击系统管理一级菜单')
        self.click_element(self.roledate[0][0], self.roledate[0][1])
        system_log.csp_log.info(f'点击账号管理二级菜单')
        self.handleform(0)
        system_log.csp_log.info(f'切换至账号管理内置表单')










