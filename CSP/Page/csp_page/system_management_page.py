from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *
from common.writeexcel import Write_Excel
system_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

csplogin_excel=ReadExcel(filepath=test_data+r'\test_login_data.xlsx',sheetname="login")
account_date=ReadExcel(filepath=test_data+r'\test_system.xlsx',sheetname="账号管理")
role_date =ReadExcel(filepath=test_data+r'\test_system.xlsx',sheetname="角色管理")
sensitive_date = ReadExcel(filepath=test_data+r'\test_system.xlsx',sheetname="敏感词库管理")

class SyStem_Management_Page(BasePage):

    user=[Write_Excel(filepath=test_data + r'\test_system.xlsx', number=0).read_column(2),
          Write_Excel(filepath=test_data + r'\test_system.xlsx', number=0).read_column(4),
          Write_Excel(filepath=test_data + r'\test_system.xlsx', number=0).read_column(5),
    ]

    add_value=[account_date.get_excel(15,5),    #0输入新增的用户名
               account_date.get_excel(16,5),    #1输入新增的用户姓名
               account_date.get_excel(17,5),    #2输入新增的身份证号
               account_date.get_excel(18,5),    #3点击上传身份证正面
               account_date.get_excel(19,5),    #4点击上传身份证反面
               account_date.get_excel(20,5),    #5选择所属角色
               account_date.get_excel(21,5),    #6选择所属区域
               account_date.get_excel(22,5),    #7输入新增的手机号码
               account_date.get_excel(23,5),    #8输入新增的邮箱
               account_date.get_excel(24,5),    #9输入新增的密码
               account_date.get_excel(10,5),    #10变更的用户名
               account_date.get_excel(26,5),    #11变更账号
               account_date.get_excel(27,5),    #12变更账号密码
               account_date.get_excel(28,5),    #13待变更账号用户姓名
               account_date.get_excel(30,5),    #14变更后得新密码
               ]

    def intouser(self):
        """
        进入账号管理二级菜单
        :return:
        """
        system_log.csp_log.info(f'开始{self.user[0][1]}')
        self.click_element(self.user[1][1],self.user[2][1])
        self.wait(0.5)
        system_log.csp_log.info(f'开始{self.user[0][2]}')
        self.click_element(self.user[1][2],self.user[2][2])
        self.wait(0.5)
        self.handleform(0)
        system_log.csp_log.info('进入账号管理内置表单')

    def find_user(self,username=add_value[0],realname=add_value[1],usertype=add_value[5],userstatus='启用'):
        """
        查询账号
        :param username:用户名
        :param realname:用户姓名
        :param usertype:所属角色
        :param userstatus：账号使用状态
        :return:
        """
        system_log.csp_log.info(f'{self.user[0][3]}-----{username}')   #输入用户名
        self.input_value(self.user[1][3],self.user[2][3],username)
        self.wait(0.5)
        system_log.csp_log.info(f'开始{self.user[0][4]}-----{realname}')   #输入用户姓名
        self.input_value(self.user[1][4], self.user[2][4],realname)
        self.wait(0.5)
        system_log.csp_log.info(f'开始{self.user[0][6]}-----{usertype}')   #选择所属角色
        self.handle_select(self.user[1][6], self.user[2][6], usertype)
        self.wait(0.5)
        system_log.csp_log.info(f'开始{self.user[0][7]}-----{userstatus}')  # 选择账号状态
        self.handle_select(self.user[1][7], self.user[2][7], userstatus)
        self.wait(0.5)
        system_log.csp_log.info(f'开始{self.user[0][8]}')  # 点击查询按钮
        self.click_element(self.user[1][8], self.user[2][8])
        self.wait(1)

    def add_user(self,newname=add_value[0],fullname=add_value[1],role=add_value[5]):
        """
        新增一个账号
        :param newname: 新增账号用户名
        :param fullname 新增账号用户姓名
        :param role     新增账号所属角色
        :return:
        """
        self.intouser()
        system_log.csp_log.info(f'{self.user[0][14]}')                 # 0点击新增按钮
        self.click_element(self.user[1][14], self.user[2][14])
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][15]}-----{newname}')   # 1输入新增的用户名
        self.input_value(self.user[1][15], self.user[2][15],newname)
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][16]}-----{fullname}')  # 2输入新增的用户姓名
        self.input_value(self.user[1][16], self.user[2][16], fullname)
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][17]}-----{self.add_value[2]}')  # 3输入新增的用户的身份证号
        self.input_value(self.user[1][17], self.user[2][17],self.add_value[2])
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][18]}-----{self.add_value[3]}')  # 4输入新增的用户身份证正面
        self.upload_file(self.user[1][18], self.user[2][18],self.add_value[3])
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][19]}-----{self.add_value[4]}')  # 5输入新增的用户身份证反面
        self.upload_file(self.user[1][19], self.user[2][19], self.add_value[4])
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][20]}-----{role}')  # 6选择新增的用户的所属角色
        self.handle_select(self.user[1][20], self.user[2][20],role)
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][21]}-----{self.add_value[6]}')  # 7选择新增的用户的所属区域
        self.handle_select(self.user[1][21], self.user[2][21], self.add_value[6])
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][22]}-----{self.add_value[7]}')  # 8输入新增的用户手机号码
        self.input_value(self.user[1][22], self.user[2][22], self.add_value[7])
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][23]}-----{self.add_value[8]}')  #9输入新增的用户邮箱
        self.input_value(self.user[1][23], self.user[2][23], self.add_value[8])
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][24]}-----{self.add_value[9]}')  #10输入新增的用户密码
        self.input_value(self.user[1][24], self.user[2][24], self.add_value[9])
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][25]}')  #11点击确认新增按钮
        self.click_element(self.user[1][25], self.user[2][25])
        self.wait(1)
        self.F5()

    def detele_user(self):
        """
        删除账号
        :return:
        """
        system_log.csp_log.info(f'{self.user[0][12]}')  # 点击删除按钮
        self.click_element(self.user[1][12], self.user[2][12])
        self.wait(0.5)
        self.F5()
    def stop_user(self):
        """
        停用账号
        :return:
        """
        system_log.csp_log.info(f'{self.user[0][13]}')  # 点击停用按钮
        self.click_element(self.user[1][13], self.user[2][13])
        self.wait(0.5)
        self.F5()

    def update_user(self,way:bool,updatename=add_value[10],updatepws=add_value[14]):
        """
        变更账号
        :param updatename:
        :return:
        """
        system_log.csp_log.info(f'{self.user[0][9]}')  # 点击编辑按钮
        self.click_element(self.user[1][9], self.user[2][9])
        self.wait(0.5)
        if way==True:
            system_log.csp_log.info(f'{self.user[0][10]}')  #清空用户名输入框
            self.clear_input(self.user[1][10], self.user[2][10])
            self.wait(0.5)
            system_log.csp_log.info(f'输入新的用户名{updatename}')  # 输入变更的用户名
            self.input_value(self.user[1][10], self.user[2][10], updatename)
            self.wait(0.5)

        elif way==False:
            system_log.csp_log.info(f'{self.user[0][30]}')
            self.clear_input(self.user[1][30],self.user[2][30])  # 清空密码输入框
            self.wait(0.5)
            system_log.csp_log.info(f'输入新密码{updatepws}')
            self.input_value(self.user[1][30],self.user[2][30],updatepws)

        system_log.csp_log.info(f'开始{self.user[0][11]}')  # 点击确认变更
        self.click_element(self.user[1][11], self.user[2][11])
        self.wait(1)
        self.F5()

    def start_user(self):
        """
        启用账号
        :return:
        """
        system_log.csp_log.info(f'开始{self.user[0][29]}')  # 点击启用按钮
        self.click_element(self.user[1][29], self.user[2][29])
        self.wait(0.5)
        self.F5()

    def refresh(self,refreshuser=add_value[11],refreshpws=add_value[12]):
        """
        复原
        :param refreshuser:
        :param refreshpws:
        :return:
        """
        system_log.csp_log.info(f'{self.user[0][9]}')  # 点击编辑按钮
        self.click_element(self.user[1][9], self.user[2][9])
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][10]}')  # 清空用户名输入框
        self.clear_input(self.user[1][10], self.user[2][10])
        self.wait(0.5)
        system_log.csp_log.info(f'输入新的用户名{refreshuser}')  # 输入变更的用户名
        self.input_value(self.user[1][10], self.user[2][10], refreshuser)
        self.wait(0.5)
        system_log.csp_log.info(f'{self.user[0][30]}')
        self.clear_input(self.user[1][30], self.user[2][30])  # 清空密码输入框
        self.wait(0.5)
        system_log.csp_log.info(f'输入新密码{refreshpws}')
        self.input_value(self.user[1][30], self.user[2][30], refreshpws)
        system_log.csp_log.info(f'开始{self.user[0][11]}')  # 点击确认变更
        self.click_element(self.user[1][11], self.user[2][11])
        self.wait(1)
        self.F5()


    def assert_text(self,text):
        """
        断言文本
        :param text:
        :return:
        """
        value  =f'<span>{text}</span>'
        return value





















