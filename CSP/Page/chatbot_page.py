from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *
from common.writeexcel import Write_Excel
from common import write_text
import time
from config import Conf
chatbot_log=Log(__name__,file=logging.INFO,cmd=logging.INFO)
search_data=ReadExcel(filepath=test_data+r'\test_chatbot_data.xlsx',sheetname="search")
add_data  =ReadExcel(filepath=test_data+r'\test_chatbot_data.xlsx',sheetname="add")
update_data  =ReadExcel(filepath=test_data+r'\test_chatbot_data.xlsx',sheetname="update")
check_data  =ReadExcel(filepath=test_data+r'\test_chatbot_data.xlsx',sheetname="check")


class  ChatbotPage(BasePage):



    searchdata=[Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=0).read_column(2),
                Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=0).read_column(4),
                Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=0).read_column(5),
                ]
    search_value = [search_data.get_excel(8,5),
                    search_data.get_excel(9,5),
                    ]

    checkdata=[Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=2).read_column(2),
               Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=2).read_column(4),
               Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=2).read_column(5)]
    check_value = [check_data.get_excel(5,5),  #选择chatbot接入类型
                   check_data.get_excel(10,5), #输入审核不通过原因
                   ]

    updatedata=[Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=1).read_column(2),  #业务操作名称
                Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=1).read_column(4),  #定位方式
                Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=1).read_column(5),  #定位表达式
                ]
    update_value=[update_data.get_excel(2,5),
                  update_data.get_excel(5,5),
                  ]

    add_msg = [Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=3).read_column(2),  #业务操作名称
               Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=3).read_column(4),  #定位方式
               Write_Excel(filepath=test_data+r'\test_chatbot_data.xlsx',number=3).read_column(5),  #定位表达式
               ]
    add_value = [add_data.get_excel(3,5),   #0输入chatbot归属csp名称
                 add_data.get_excel(8,5),   #1输入chatbot归属企业客户名称
                 add_data.get_excel(12,5),  #2输入新建的Chatbot名称
                 add_data.get_excel(14,5),  #3点击上传chatbot头像按钮
                 add_data.get_excel(17,5),  #4选择行业类型
                 add_data.get_excel(20,5),  #5输入Chatbot邮箱
                 add_data.get_excel(21,5),  #6输入Chatbot官网
                 add_data.get_excel(22,5),  #7输入Chatbot服务电话
                 add_data.get_excel(23,5),  #8选择省份
                 add_data.get_excel(24,5),  #9选择地市
                 add_data.get_excel(25,5),  #10选择县区
                 add_data.get_excel(26,5),  #11输入具体地址
                 add_data.get_excel(27,5),  #12输入纬度
                 add_data.get_excel(28,5),  #13输入经度
                 add_data.get_excel(29,5)]  #14输入ip地址

    nowtime = time.strftime('%Y-%m-%d %H:%M:%S')


    def intoform(self):
        """
        进入csp管理二级菜单内置表单
        :return:
        """
        chatbot_log.csp_log.info(f'进入chatbot管理内置表单---------开始{self.searchdata[0][1]}')
        self.click_element(self.searchdata[1][1],self.searchdata[2][1])
        chatbot_log.csp_log.info(f'进入chatbot管理内置表单---------开始{self.searchdata[0][2]}')
        self.click_element(self.searchdata[1][2],self.searchdata[2][2])
        self.handleform(0)
        chatbot_log.csp_log.info('进入内置表单')

    def add_chatbot(self,name=add_value[2]):
        """
        新增一个chatbot
        :param name:
        :return:
        """
        try:
            self.intoform()  #进入内置表单
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][1]}')
            self.click_element(self.add_msg[1][1],self.add_msg[2][1])  #点击新增chatbot按钮
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][2]}')
            self.click_element(self.add_msg[1][2],self.add_msg[2][2])  #点击归属CSP按钮
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][3]}')
            self.input_value(self.add_msg[1][3],self.add_msg[2][3],self.add_value[0])    #输入csp名称
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][4]}')
            self.click_element(self.add_msg[1][4],self.add_msg[2][4])  #点击查询按钮
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][5]}')
            self.click_element(self.add_msg[1][5],self.add_msg[2][5])  #点击选择csp
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][6]}')
            self.click_element(self.add_msg[1][6],self.add_msg[2][6])  #点击确认选择
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][7]}')
            self.click_element(self.add_msg[1][7],self.add_msg[2][7])  #点击选择客户
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][8]}')
            self.input_value(self.add_msg[1][8],self.add_msg[2][8],self.add_value[1])  #输入企业客户名称
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][9]}')
            self.click_element(self.add_msg[1][9],self.add_msg[2][9])  #点击查询按钮
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][10]}')
            self.click_element(self.add_msg[1][10],self.add_msg[2][10])  #点击选择某一个客户
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][11]}')
            self.click_element(self.add_msg[1][11],self.add_msg[2][11])  #点击确认选择
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][12]}')
            self.input_value(self.add_msg[1][12],self.add_msg[2][12],name)  #输入新建的chatbot名称
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][13]}')
            self.input_value(self.add_msg[1][13],self.add_msg[2][13],self.random_number())  #输入cahtbotid
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][14]}')
            self.upload_file(self.add_msg[1][14],self.add_msg[2][14],self.add_value[3])  #上传chatbot头像
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][15]}')
            self.input_value(self.add_msg[1][15],self.add_msg[2][15],self.random_number())  #输入服务信息
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][16]}')
            self.input_value(self.add_msg[1][16],self.add_msg[2][16],self.random_number())  #输入签名
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][17]}')
            self.handle_select(self.add_msg[1][17],self.add_msg[2][17],self.add_value[4])  #选择行业类型
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][19]}')
            self.input_value(self.add_msg[1][19],self.add_msg[2][19],self.random_number()) #输入服务条款
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][20]}')
            self.input_value(self.add_msg[1][20],self.add_msg[2][20],self.add_value[5])  #输入Chatbot邮箱
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][21]}')
            self.input_value(self.add_msg[1][21],self.add_msg[2][21],self.add_value[6])  #输入Chatbot官网
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][22]}')
            self.input_value(self.add_msg[1][22],self.add_msg[2][22],self.add_value[7])  #输入Chatbot服务电话
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][23]}')
            self.handle_select(self.add_msg[1][23],self.add_msg[2][23], self.add_value[8]) #选择省份
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][24]}')
            self.handle_select(self.add_msg[1][24],self.add_msg[2][24], self.add_value[9]) #选择地市
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][25]}')
            self.handle_select(self.add_msg[1][25],self.add_msg[2][25], self.add_value[10]) #选择县区
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][26]}')
            self.input_value(self.add_msg[1][26],self.add_msg[2][26],self.add_value[11])   #输入具体地址
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][27]}')
            self.input_value(self.add_msg[1][27],self.add_msg[2][27], self.add_value[12])   #输入纬度
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][28]}')
            self.input_value(self.add_msg[1][28],self.add_msg[2][28], self.add_value[13])   #输入经度
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][29]}')
            self.input_value(self.add_msg[1][29],self.add_msg[2][29], self.add_value[14])   #输入ip地址
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot新增页面------开始{self.add_msg[0][32]}')
            self.click_element(self.add_msg[1][32],self.add_msg[2][32])  #点击确认新增
            self.wait(2)
        except Exception:
            chatbot_log.csp_log.exception(f'新增cahtbot--{name}失败')
            raise
        else:
            chatbot_log.csp_log.info(f'新增cahtbot--{name}成功')
            write_text.Text_action(Conf.notebook + r'\notebook.txt').write_file(value=f'{self.nowtime}-----{name}')
        finally:
               self.F5()


    def find_chatbot(self,chatbotname=add_value[2]):
        """
        csp管理二级菜单输入chatbot名称和选择chatbot接入类型查询数据
        :param chatbotname:
        :return:
        """
        self.intoform()
        chatbot_log.csp_log.info(f'chatbot管理查询页面----------开始{self.searchdata[0][4]}')
        self.input_value(self.searchdata[1][4],self.searchdata[2][4],chatbotname)  #输入chatbot名称
        self.wait(1)
        chatbot_log.csp_log.info(f'chatbot管理查询页面----------开始{self.searchdata[0][8]}')
        self.handle_select(self.searchdata[1][8],self.searchdata[2][8],self.search_value[0]) #选择chatbot接入类型
        self.wait(1)
        chatbot_log.csp_log.info(f'chatbot管理查询页面----------开始{self.searchdata[0][10]}')
        self.click_element(self.searchdata[1][10],self.searchdata[2][10])  #点击查询按钮
        self.wait(1)

    def into_lookover(self):
        """
        点击查看按钮
        :return:
        """
        chatbot_log.csp_log.info(f'chatbot管理查询页面----------开始{self.searchdata[0][11]}')
        self.click_element(self.searchdata[1][11],self.searchdata[2][11])  #点击查看按钮
        self.wait(1)



    def update_name(self):
        """
        变更chatbot名称
        :return:
        """
        try:
            chatbot_log.csp_log.info(f'chatbot信息查看页面-------开始{self.searchdata[0][1]}')
            self.click_element(self.updatedata[1][1], self.updatedata[2][1])  # 点击chatbot信息编辑按钮
            self.wait(1)
            chatbot_log.csp_log.info(f'清空输入框')
            self.clear_input(self.updatedata[1][2], self.updatedata[2][2])  # 清空chatbot名称输入框
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot信息查看页面-------开始{self.searchdata[0][2]}')
            self.input_value(self.updatedata[1][2], self.updatedata[2][2],self.update_value[0])  # 输入新的chatbot名称
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot信息查看页面-------开始{self.searchdata[0][3]}')
            self.click_element(self.updatedata[1][3], self.updatedata[2][3])  # 点击确认变更按钮
            self.wait(1)
        except Exception:
            chatbot_log.csp_log.exception('客户名称变更失败')
            raise
        else:
            chatbot_log.csp_log.info('客户名称变更成功')
            self.F5()

    def update_speed(self):
        """
        变更chatbot速率
        :return:
        """
        try:
            chatbot_log.csp_log.info(f'chatbot信息查看页面-------开始{self.searchdata[0][4]}')
            self.click_element(self.updatedata[1][4],self.updatedata[2][4])   #点击chatbot配置编辑按钮
            self.wait(1)
            chatbot_log.csp_log.info(f'清空输入框')
            self.clear_input(self.updatedata[1][5],self.updatedata[2][5])    #清空chatbot信息发送速率输入框
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot信息查看页面-------开始{self.searchdata[0][5]}')
            self.input_value(self.updatedata[1][5],self.updatedata[2][5],self.update_value[1]) #输入变更的chatbot速率
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot信息查看页面-------开始{self.searchdata[0][6]}')
            self.click_element(self.updatedata[1][6],self.updatedata[2][6])  #点击确认变更按钮
            self.wait(2)

        except Exception:
            chatbot_log.csp_log.exception('chatbot速率变更失败')
            raise
        else:
            chatbot_log.csp_log.info('cahtbot速率变更成功')
            self.F5()

    def delete_chatbot(self):
        """
        注销chatbot
        :return:
        """
        try:
            chatbot_log.csp_log.info(f'chatbot信息查看页面-------开始{self.searchdata[0][7]}')
            self.click_element(self.updatedata[1][7],self.updatedata[2][7])   #点击注销chatbot按钮
            self.wait(1)
            chatbot_log.csp_log.info(f'chatbot信息查看页面-------开始{self.searchdata[0][8]}')
            self.click_element(self.updatedata[1][8],self.updatedata[2][8])   #点击确认注销
            self.wait(1)
        except Exception:
            chatbot_log.csp_log.exception('chatbot注销失败')
            raise
        else:
            chatbot_log.csp_log.info('chatbot注销成功')
            self.F5()

    def intocheck(self,way='0'):
        """
        进入chatbot审核内置表单
        :param way:默认需要身份验证
        :return:
        """
        chatbot_log.csp_log.info(f'进入chatbot审核内置表单------开始{self.checkdata[0][1]}')
        self.click_element(self.searchdata[1][1],self.searchdata[2][1])
        self.wait(1)
        chatbot_log.csp_log.info(f'进入chatbot审核内置表单------开始{self.checkdata[0][1]}')
        self.click_element(self.checkdata[1][1],self.checkdata[2][1])
        self.wait(1)
        self.handleform(0)
        # 判断页面是否存在身份验证
        if way == '0':
            self.click_element(self.checkdata[1][12],self.checkdata[2][12])
            chatbot_log.csp_log.info(f'开始---------{self.checkdata[0][12]}')
            self.wait(30)
            self.click_element(self.checkdata[1][13],self.checkdata[2][13])
            chatbot_log.csp_log.info(f'开始---------{self.checkdata[0][13]}')
            self.wait(2)
        else:
            chatbot_log.csp_log.info(f'不需要身份验证进入chatbot审核二级表单')


    def find_check(self,check_chatbotname=add_value[2],check_type='信息创建'):
        """
        查询出待审核的chatbot
        :param check_chatbotname:带查询的chatbot名称
        :param check_type: 带查询的chatbot审核类型
        :return:
        """
        chatbot_log.csp_log.info(f'查询待审核的chatbot数据------开始{self.checkdata[0][4]}')
        self.input_value(self.checkdata[1][4], self.checkdata[2][4],check_chatbotname)  # 输入待审核的chatbot名称
        self.wait(1)
        chatbot_log.csp_log.info(f'查询待审核的chatbot数据------开始{self.checkdata[0][5]}')
        self.handle_select(self.checkdata[1][5], self.checkdata[2][5],self.check_value[0])  # 选择接入类型
        self.wait(1)
        chatbot_log.csp_log.info(f'查询待审核的chatbot数据------开始---------{self.checkdata[0][6]}')
        self.handle_select(self.checkdata[1][6],self.checkdata[2][6],check_type)  #选择审核类型
        self.wait(1)
        chatbot_log.csp_log.info(f'查询待审核的chatbot数据------开始---------{self.checkdata[0][14]}')
        self.input_value(self.checkdata[1][14],self.checkdata[2][14],self.add_value[1])
        self.wait(1)
        chatbot_log.csp_log.info(f'查询待审核的chatbot数据------开始{self.checkdata[0][7]}')
        self.click_element(self.checkdata[1][7], self.checkdata[2][7])  # 点击查询按钮
        self.wait(1)



    def assert_chatbotname(self,chatbot_name=add_value[2]):
        """
        判断某个节点chatbot名称是否存在
        :param chatbot_name:
        :return:
        """

        value = f'<td>{chatbot_name}</td>'
        return value

    def check_chatbot(self,result='0'):
        """
        开始审核chatbot
        :param result: 默认审核通过
        :return:
        """
        chatbot_log.csp_log.info(f'查询待审核的chatbot数据------开始{self.checkdata[0][8]}')
        self.click_element(self.checkdata[1][8],self.checkdata[2][8])  #点击审核按钮
        if result=='0':   #审核通过
            try:
                self.click_element(self.checkdata[1][11], self.checkdata[2][11])  # 点击确认审核
                chatbot_log.csp_log.info(f'开始---------{self.checkdata[0][11]}')
                self.wait(2)
            except Exception:
                chatbot_log.csp_log.exception('审核失败')
                raise
            else:
                chatbot_log.csp_log.info(f'审核通过')
            finally:
                self.F5()

        elif result !='0':  #审核不通过
            try:
                chatbot_log.csp_log.info(f'chatbot审核页面---------开始{self.checkdata[0][9]}')
                self.click_element(self.checkdata[1][9],self.checkdata[2][9])  #点击审核不通过
                self.wait(1)
                chatbot_log.csp_log.info(f'chatbot审核页面---------开始---------{self.checkdata[0][10]}')
                self.input_value(self.checkdata[1][10],self.checkdata[2][10],self.check_value[1])  #输入审核不通过原因
                self.wait(1)
                chatbot_log.csp_log.info(f'chatbot审核页面---------开始---------{self.checkdata[0][11]}')
                self.click_element(self.checkdata[1][11], self.checkdata[2][11])  # 点击确认审核
                self.wait(1)
            except Exception:
                chatbot_log.csp_log.exception('审核失败')
                raise
            else:
                chatbot_log.csp_log.info('审核成功')
            finally:
                self.F5()


    def assert_chatbot_rate(self,chatbot_rate=update_value[1]):
        """
        变更Chatbot速率获取标签文本值
        :return:
        """
        rate = f'<div>{chatbot_rate}</div>'
        return rate





























