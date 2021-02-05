from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *
from common import write_text
from config import Conf
import time
from common.writeexcel import Write_Excel
custmoer_log=Log(__name__,file=logging.INFO,cmd=logging.INFO)
add_data=ReadExcel(filepath=test_data+r'\test_customer_data.xlsx',sheetname="add")
search_data=ReadExcel(filepath=test_data+r'\test_customer_data.xlsx',sheetname="search")
update_data = ReadExcel(filepath=test_data+r'\test_customer_data.xlsx',sheetname="update")
check_data = ReadExcel(filepath=test_data+r'\test_customer_data.xlsx',sheetname="check")

class CustmoerPage(BasePage):


    add = [Write_Excel(filepath=test_data+r'\test_customer_data.xlsx',number=3).read_column(2),
           Write_Excel(filepath=test_data+r'\test_customer_data.xlsx',number=3).read_column(4),
           Write_Excel(filepath=test_data+r'\test_customer_data.xlsx',number=3).read_column(5),
           ]
    add_value = [add_data.get_excel(2,5),  #0输入新增的客户名称
                 add_data.get_excel(3,5),  #1操作选择所属csp下拉框
                 add_data.get_excel(4,5),  #2上传企业logo
                 add_data.get_excel(5,5),  #3上传营业执照
                 add_data.get_excel(6,5),  #4输入企业介绍
                 add_data.get_excel(7,5),  #5输入企业所在地
                 add_data.get_excel(8,5),  #6处理行业类型下拉框
                 add_data.get_excel(9,5),  #7处理客户等级下拉框
                 add_data.get_excel(10,5), #8输入企业法人
                 add_data.get_excel(11,5), #9输入企业法人身份证号
                 add_data.get_excel(12,5), #10上传企业法人身份证正面
                 add_data.get_excel(13,5), #11上传企业法人身份证反面
                 add_data.get_excel(14,5), #12输入客户联系人姓名
                 add_data.get_excel(15,5), #13输入客户联系人电话
                 add_data.get_excel(16,5), #14输入客户联系人邮箱
                 add_data.get_excel(17,5), #15输入客户联系人身份证号
                 add_data.get_excel(18,5), #16上传客户联系人身份证正面
                 add_data.get_excel(19,5), #17上传客户联系人身份证反面
                 add_data.get_excel(21,5), #18输入合同名称
                 add_data.get_excel(22,5), #19输入合同生效日期
                 add_data.get_excel(23,5), #20输入合同失效日期
                 add_data.get_excel(25,5), #21输入合同续约日期
                 add_data.get_excel(26,5), #22上传合同附件
                 add_data.get_excel(28,5), #23输入办公电话
                 ]

    search = [Write_Excel(filepath=test_data+r'\test_customer_data.xlsx',number=0).read_column(2),
              Write_Excel(filepath=test_data + r'\test_customer_data.xlsx', number=0).read_column(4),
              Write_Excel(filepath=test_data + r'\test_customer_data.xlsx', number=0).read_column(5),
              search_data.get_excel(6,5),
              ]

    check = [Write_Excel(filepath=test_data+r'\test_customer_data.xlsx',number=2).read_column(2),
             Write_Excel(filepath=test_data + r'\test_customer_data.xlsx', number=2).read_column(4),
             Write_Excel(filepath=test_data + r'\test_customer_data.xlsx', number=2).read_column(5),
             check_data.get_excel(9,5),check_data.get_excel(10,5),check_data.get_excel(14,5),
             ]

    update_user=[Write_Excel(filepath=test_data+r'\test_customer_data.xlsx',number=1).read_column(2),
                 Write_Excel(filepath=test_data+r'\test_customer_data.xlsx',number=1).read_column(4),
                 Write_Excel(filepath=test_data+r'\test_customer_data.xlsx',number=1).read_column(5),
                 update_data.get_excel(2,5),
                 update_data.get_excel(3,5),
                 ]


    nowtime = time.strftime('%Y-%m-%d %H:%M:%S')


    def intoform(self):
        """
        进入客户管理二级菜单查询节点
        :return:
        """
        try:
            custmoer_log.csp_log.info(f'进入客户管理内置表单----------开始{self.search[0][1]}')
            self.click_element(self.search[1][1],self.search[2][1])
            custmoer_log.csp_log.info(f'进入客户管理内置表单----------开始{self.search[0][2]}')
            self.click_element(self.search[1][2],self.search[2][2])
            custmoer_log.csp_log.info(f'开始{self.search[0][2]}')
            self.handleform(0)

        except Exception:
            custmoer_log.csp_log.exception('进入客户管理二级菜单失败')
            raise
        else:
            custmoer_log.csp_log.info('点击客户管理二级菜单内嵌表单')


    def find_name(self,customername=add_value[0],belog_csp=check[4]):
        """
        按客户名称和客户类型查询数据
        :param customername: 查询的客户名称
        :param belog_csp: 查询的客户归属csp
        :return:
        """
        self.intoform()
        self.wait(1)
        try:
            custmoer_log.csp_log.info(f'客户信息查询--------------开始{self.search[0][3]}--------{customername}')
            self.input_value(self.search[1][3],self.search[2][3],customername)
            self.wait(1)
            custmoer_log.csp_log.info(f'客户信息查询--------------开始{self.search[0][6]}----------{self.search[3]}')
            self.handle_select(self.search[1][6],self.search[2][6],self.search[3])
            self.wait(1)
            custmoer_log.csp_log.info(f'客户信息查询--------------开始{self.check[0][9]}-----------{belog_csp}')
            self.input_value(self.search[1][9], self.search[2][9],belog_csp)
            self.wait(1)
            custmoer_log.csp_log.info(f'客户信息查询--------------开始{self.search[0][7]}')
            self.click_element(self.search[1][7],self.search[2][7])  #点击查询按钮
            self.wait(1)
        except Exception:
            custmoer_log.csp_log.exception(f'查询客户----{customername}失败')
            raise
        else:
            custmoer_log.csp_log.info(f'查询客户----{customername}成功')

    def look_user(self):
        """
        点击查看客户信息
        :return:
        """
        try:
            self.click_element(self.search[1][8],self.search[2][8])
            self.wait(1)

        except Exception:
            custmoer_log.csp_log.exception(f'查询客户----开始{self.search[0][8]} 失败')
            raise
        else:
            custmoer_log.csp_log.info(f'查询客户----开始{self.search[0][8]} 成功')

    def delete_user(self):
        """
        注销客户
        :return:
        """
        self.look_user() #点击查看按钮
        try:
            custmoer_log.csp_log.info(f'客户信息查看页面------------开始{self.search[0][12]}')
            self.click_element(self.search[1][12],self.search[2][12])  #点击注销按钮
            self.wait(1)
            custmoer_log.csp_log.info(f'客户信息查看页面------------开始{self.search[0][13]}')
            self.click_element(self.search[1][13],self.search[2][13])  #点击确认注销按钮
            self.wait(1)
            self.F5()
        except Exception:
            custmoer_log.csp_log.exception(f'注销客户失败')
        else:
            custmoer_log.csp_log.info('注销客户成功')

    def add_customer(self,name=add_value[0]):
        """
        新增客户
        :param name: 新增的客户名称
        :return:
        """
        try:
            self.intoform()
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][1]}')
            self.click_element(self.add[1][1],self.add[2][1])
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][2]}-------{name}')
            self.input_value(self.add[1][2],self.add[2][2],name)  #输入客户名称
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][3]}')
            self.handle_select(self.add[1][3],self.add[2][3],self.add_value[1])   #操作选择所属csp下拉框
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][4]}')
            self.upload_file(self.add[1][4],self.add[2][4],self.add_value[2])   #上传企业logo
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][5]}')
            self.upload_file(self.add[1][5],self.add[2][5],self.add_value[3])   #上传营业执照
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][6]}')
            self.input_value(self.add[1][6],self.add[2][6],self.add_value[4])  #输入企业介绍
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][7]}-------{self.add_value[5]}')
            self.input_value(self.add[1][7],self.add[2][7],self.add_value[5])   #输入企业所在地
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][8]}-------{self.add_value[6]}')
            self.handle_select(self.add[1][8],self.add[2][8],self.add_value[6])   #处理行业类型下拉框
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][28]}-----------{self.add_value[23]}')
            self.input_value(self.add[1][28],self.add[2][28],self.add_value[23])  #输入办公电话
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][9]}-------{self.add_value[7]}')
            self.handle_select(self.add[1][9],self.add[2][9],self.add_value[7])  #处理客户等级下拉框
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][10]}------{self.add_value[8]}')
            self.input_value(self.add[1][10],self.add[2][10],self.add_value[8]) #输入企业法人
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][11]}--------{self.add_value[9]}')
            self.input_value(self.add[1][11],self.add[2][11],self.add_value[9]) #输入企业法人身份证号
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][12]}---------{self.add_value[10]}')
            self.upload_file(self.add[1][12],self.add[2][12],self.add_value[10]) #上传企业法人身份证正面
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][13]}---------{self.add_value[11]}')
            self.upload_file(self.add[1][13],self.add[2][13],self.add_value[11]) #上传企业法人身份证反面
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][14]}----------{self.add_value[12]}')
            self.input_value(self.add[1][14],self.add[2][14],self.add_value[12]) #输入客户联系人姓名
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][15]}')
            self.input_value(self.add[1][15],self.add[2][15],self.add_value[13]+self.random_number()) #输入客户联系人电话
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][16]}------------{self.add_value[14]}')
            self.input_value(self.add[1][16],self.add[2][16],self.add_value[14]) #输入客户联系人邮箱
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][17]}')
            self.input_value(self.add[1][17],self.add[2][17],self.add_value[15]) #输入客户联系人身份证号
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][18]}')
            self.upload_file(self.add[1][18],self.add[2][18],self.add_value[16])  #上传客户联系人身份证正面
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][19]}')
            self.upload_file(self.add[1][19],self.add[2][19],self.add_value[17])  #上传客户联系人身份证反面
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][20]}')
            self.input_value(self.add[1][20],self.add[2][20],self.random_number())  #输入合同编号
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][21]}--------{self.add_value[18]}')
            self.input_value(self.add[1][21],self.add[2][21],self.add_value[18])    #输入合同名称
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][22]}')
            self.jsp(self.add[2][22]) #输入合同生效日期
            self.wait(1)
            self.jsp(self.add_value[19])
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][23]}')
            self.jsp(self.add[2][23]) #输入合同失效日期
            self.wait(1)
            self.jsp(self.add_value[20])
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][25]}')
            self.jsp(self.add[2][25]) #输入合同续约日期
            self.wait(1)
            self.jsp(self.add_value[21])
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][26]}')
            self.upload_file(self.add[1][26],self.add[2][26],self.add_value[22])  #上传合同附件
            self.wait(1)
            custmoer_log.csp_log.info(f'客户新增页面-----------开始{self.add[0][27]}')
            self.click_element(self.add[1][27],self.add[2][27])  #点击确认新建客户按钮
            self.wait(1)

        except Exception:
            custmoer_log.csp_log.exception(f'新增客户---{name}失败')
            raise
        else:

            write_text.Text_action(Conf.notebook+r'\notebook.txt').write_file(value=f'{self.nowtime}-----{name}')
            self.F5()
            custmoer_log.csp_log.info(f'新增客户-----{name}成功')



    def intoformcheck(self,intoway='0'):
        """
        进入客户审核二级菜单内嵌表单页面
        :param way:
        :return:
        """
        try:
            custmoer_log.csp_log.info(f'进入客户审核内置表单-----------开始{self.search[0][1]}')
            self.click_element(self.search[1][1], self.search[2][1])
            custmoer_log.csp_log.info(f'进入客户审核内置表单-----------开始{self.check[0][2]}')
            self.click_element(self.check[1][1],self.check[2][1])
            self.handleform(0)
        except Exception:
            custmoer_log.csp_log.exception('进入客户审核二级菜单失败')
            raise
        else:
            custmoer_log.csp_log.info('进入客户审核二级菜单成功')
            # 判断页面是否存在身份验证
            if intoway=='0':

                if self.isElementExist(findway=self.check[1][18],elementvalue=self.check[2][18]):
                    self.wait(40)
                    self.click_element(self.check[1][19], self.check[2][19])
                    self.wait(5)
                else:
                    custmoer_log.csp_log.info(f'开始{self.check[0][19]}')
            else:
                custmoer_log.csp_log.info(f'身份验证成功')

    def finding_check(self,way='0',checkname=add_value[0],way_number='0',check_way=check[3]):
        """
        查询已审核或者未审核的客户数据
        :param way: 判断查询已审核还是待审核数据
        :param checkname: 查询的客户名称
        :param way_number: 判断是否需要身份严重
        :param check_way: 判读查询的数据审核类型
        :return:
        """

        self.intoformcheck(intoway=way_number)#点击进入审核内置表单

        if way == '0':
            custmoer_log.csp_log.info('默认选择待审核')
        elif way == '1':
            custmoer_log.csp_log.info(f'查询审核的数据---------开始{self.check[0][16]}')
            self.click_element(self.check[1][16], self.check[2][16])  ##点击已审核
            self.wait(1)

        try:
            custmoer_log.csp_log.info(f'查询审核的数据---------开始{self.check[0][6]}')
            self.input_value(self.check[1][6], self.check[2][6], checkname)  # 输入客户名称
            self.wait(1)
            custmoer_log.csp_log.info(f'查询审核的数据---------开始{self.check[0][9]}')
            self.handle_select(self.check[1][9], self.check[2][9],check_way)
            self.wait(1)
            custmoer_log.csp_log.info(f'查询审核的数据---------开始{self.check[0][10]}')
            self.handle_select(self.check[1][10], self.check[2][10], self.check[4])
            self.wait(1)
            custmoer_log.csp_log.info(f'查询审核的数据---------开始{self.check[0][11]}')
            self.click_element(self.check[1][11], self.check[2][11])  # 点击查询按钮
            self.wait(1)
        except Exception:
            custmoer_log.csp_log.exception(f'查询待审核的客户数据--------{checkname}失败')
        else:
            custmoer_log.csp_log.info(f'查询待审核的客户数据--------{checkname}成功')


    def click_check(self,result='0'):
        """
        若查询出待审核数据点击审核按钮开始审核
        :param result:默认审核通过
        :return:
        """
        custmoer_log.csp_log.info(f'查询审核的数据---------开始{self.check[0][12]}')
        self.click_element(self.check[1][12],self.check[2][12])  #点击审核按钮
        self.wait(1)
        if result == '1':
            try:
                custmoer_log.csp_log.info(f'客户信息审核页面-----------开始{self.check[0][13]}')
                self.click_element(self.check[1][13],self.check[2][13])  #点击审核不通过
                self.wait(1)
                custmoer_log.csp_log.info(f'客户信息审核页面-----------开始{self.check[5]}')
                self.input_value(self.check[1][14],self.check[2][14],self.check[5])  #输入审核不通过原因
                self.wait(1)
                custmoer_log.csp_log.info(f'开始{self.check[0][15]}')
                self.click_element(self.check[1][15], self.check[2][15])  # 点击确认审核按钮
                self.wait(1)
            except Exception:
                custmoer_log.csp_log.exception(f'审核失败')
                raise
            else:
                custmoer_log.csp_log.info('审核成功')
            finally:
                   self.F5()

        else:
            custmoer_log.csp_log.info(f'客户信息审核页面-----------开始{self.check[0][15]}')
            self.click_element(self.check[1][15], self.check[2][15])  # 点击确认审核按钮
            self.wait(1)
            self.F5()

    def assert_text(self,text):
        """

        :param text:
        :return:
        """
        value = f'<td>{text}</td>'
        return value

    def update_msg(self):
        """
        变更客户信息
        :return:
        """
        self.look_user()  # 点击查看按钮
        self.wait(1)
        custmoer_log.csp_log.info(f'客户信息查看页面-------开始{self.update_user[0][1]}')
        self.click_element(self.update_user[1][1],self.update_user[2][1])
        self.wait(1)
        custmoer_log.csp_log.info(f'客户信息查看页面-------开始{self.update_user[0][2]}')
        self.clear_input(self.update_user[1][2],self.update_user[2][2])
        self.wait(1)
        custmoer_log.csp_log.info(f'客户信息查看页面-------开始{self.update_user[0][2]}-----------{self.update_user[3]}')
        self.input_value(self.update_user[1][2],self.update_user[2][2],self.update_user[3])
        self.wait(1)
        custmoer_log.csp_log.info(f'客户信息查看页面-------开始{self.update_user[0][4]}')
        self.click_element(self.update_user[1][4],self.update_user[2][4])
        self.wait(1)
        self.F5()






























