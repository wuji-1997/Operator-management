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


    accountdate=[(account_date.get_excel(1,3),account_date.get_excel(1,4)),    #点击系统管理
                 (account_date.get_excel(2,3),account_date.get_excel(2,4)),   #点击账号管理
                 (account_date.get_excel(3,3),account_date.get_excel(3,4)),  #输入用户名
                 (account_date.get_excel(4,3),account_date.get_excel(4,4)),  #输入用户姓名
                 (account_date.get_excel(5,3),account_date.get_excel(5,4)),  #输入手机号
                 (account_date.get_excel(6,3),account_date.get_excel(6,4)),  #选择所属角色
                 (account_date.get_excel(7,3),account_date.get_excel(7,4)),  #选择角色状态
                 (account_date.get_excel(8,3),account_date.get_excel(8,4)),  #点击查询按钮
                 (account_date.get_excel(9,3),account_date.get_excel(9,4)),  #点击编辑按钮
                 (account_date.get_excel(10,3),account_date.get_excel(10,4),account_date.get_excel(10,5)),  #变更用户名
                 (account_date.get_excel(11,3),account_date.get_excel(11,4),account_date.get_excel(11,5)),  #点击确认变更按钮
                 (account_date.get_excel(12,3),account_date.get_excel(12,4)),  #点击删除按钮
                 (account_date.get_excel(13,3),account_date.get_excel(13,4)),  #点击停用按钮
                 (account_date.get_excel(14,3),account_date.get_excel(14,4)),  #点击新增账号按钮
                 (account_date.get_excel(15,3),account_date.get_excel(15,4),account_date.get_excel(15,5)),  #输入新增的用户名
                 (account_date.get_excel(16,3),account_date.get_excel(16,4),account_date.get_excel(16,5)),  #输入新增的用户姓名
                 (account_date.get_excel(17,3),account_date.get_excel(17,4),account_date.get_excel(17,5)),  #输入新增的身份证号
                 (account_date.get_excel(18,3),account_date.get_excel(18,4),account_date.get_excel(18,5)),  #点击上传身份证正面
                 (account_date.get_excel(19,3),account_date.get_excel(19,4),account_date.get_excel(19,5)),  #点击上传身份证反面
                 (account_date.get_excel(20,3),account_date.get_excel(20,4),account_date.get_excel(20,5)),  #选择所属角色
                 (account_date.get_excel(21,3),account_date.get_excel(21,4),account_date.get_excel(21,5)),  #选择所属区域
                 (account_date.get_excel(22,3),account_date.get_excel(22,4),account_date.get_excel(22,5)),  #输入新增的手机号码
                 (account_date.get_excel(23,3),account_date.get_excel(23,4),account_date.get_excel(23,5)),  #输入新增的邮箱
                 (account_date.get_excel(24,3),account_date.get_excel(24,4),account_date.get_excel(24,5)),  #输入新增的密码
                 (account_date.get_excel(25,3),account_date.get_excel(25,4)),  #点击确认新增按钮
                 ]

    roledate=[(role_date.get_excel(1,3),role_date.get_excel(1,4)),   #点击角色管理
              (role_date.get_excel(2,3),role_date.get_excel(2,4)),   #输入角色名称
              (role_date.get_excel(3,3),role_date.get_excel(3,4)),   #点击查询按钮
              (role_date.get_excel(4,3),role_date.get_excel(4,4)),   #点击编辑按钮
              (role_date.get_excel(5,3),role_date.get_excel(5,4),role_date.get_excel(5,5)), #输入变更角色名称
              (role_date.get_excel(6,3),role_date.get_excel(6,4)),   #点击确认变更按钮
              (role_date.get_excel(7,3),role_date.get_excel(7,4)),   #点击删除按钮
              (role_date.get_excel(8,3),role_date.get_excel(8,4)),   #点击复制按钮
              (role_date.get_excel(9,3),role_date.get_excel(9,4),role_date.get_excel(9,5)),  #输入复制的角色名称
              (role_date.get_excel(10,3),role_date.get_excel(10,4)),  #点击新增角色
              (role_date.get_excel(11,3),role_date.get_excel(11,4),role_date.get_excel(11,5)),  #输入新增角色名称
              (role_date.get_excel(12,3),role_date.get_excel(12,4),role_date.get_excel(12,5)),  #输入新增角色权限描述
              ]

    sensitivedate=[(sensitive_date.get_excel(1,3),sensitive_date.get_excel(1,4)),   #点击敏感词库管理
                   (sensitive_date.get_excel(2,3),sensitive_date.get_excel(2,4)),   #点击新增字词
                   (sensitive_date.get_excel(3,3),sensitive_date.get_excel(3,4),sensitive_date.get_excel(3,5)), #输入敏感字词
                   (sensitive_date.get_excel(4,3),sensitive_date.get_excel(4,4)),  #点击确认新增按钮
                   (sensitive_date.get_excel(5,3),sensitive_date.get_excel(5,4)),  #输入关键字
                   (sensitive_date.get_excel(6,3),sensitive_date.get_excel(6,4)),  #点击查询按钮
                   (sensitive_date.get_excel(7,3),sensitive_date.get_excel(7,4)),  #点击编辑按钮
                   (sensitive_date.get_excel(8,3),sensitive_date.get_excel(8,4),sensitive_date.get_excel(8,5)), #输入变更的敏感字词
                   (sensitive_date.get_excel(9,3),sensitive_date.get_excel(9,4)), #点击确认变更按钮
                   (sensitive_date.get_excel(10,3),sensitive_date.get_excel(10,4)), #点击删除按钮
                   ]



