from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *
from common.writeexcel import Write_Excel
from common import write_text
import time
from config import Conf
from selenium.webdriver.common.by import By
csp_log = Log(__name__, file=logging.INFO, cmd=logging.INFO)

add_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="add")
search_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="search")
check_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="check")
update_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="update")
other_add = ReadExcel(filepath=test_data + r'\add_csp.xlsx', sheetname='CSP信息申请模板')
grounding_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="grounding")


class CspPage(BasePage):

    search = [Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=0).read_column(2),
              Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=0).read_column(4),
              Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=0).read_column(5),
              ]
    search_value = [search_data.get_excel(5, 5),  # 0CSP类型下拉框处理
                    search_data.get_excel(6, 5),  # 1CSP状态下拉框处理
                    search_data.get_excel(7, 5),  # 2CSP所属省份下拉框处理
                    search_data.get_excel(12,5),  # 3点击上传测试报告稿
                   ]
    add=[Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=1).read_column(2),
         Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=1).read_column(4),
         Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=1).read_column(5),
         ]

    add_value=[add_data.get_excel(2, 5),  # 0输入新增的CSP名称
               add_data.get_excel(3, 5),  # 1选择新增的CSP客户类型
               add_data.get_excel(4, 5),  # 2选择csp类型
               add_data.get_excel(5, 5),  # 3选择csp归属省份
               add_data.get_excel(6, 5),  # 4选择csp归属地市
               add_data.get_excel(7, 5),  # 5输入新增的CSP联系人
               add_data.get_excel(8, 5),  # 6输入新增的CSP联系电话
               add_data.get_excel(9, 5),  # 7输入新增的CSP联系人身份证号
               add_data.get_excel(10, 5), # 8输入新增的CSP联系人邮箱
               add_data.get_excel(11, 5), # 9上传新增的CSP的经办人身份证正面
               add_data.get_excel(12, 5), # 10上传新增的CSP的经办人身份证反面
               add_data.get_excel(13, 5), # 11输入IP地址
               add_data.get_excel(14, 5), # 12输入CSP回调根目录地址
               add_data.get_excel(16, 5), # 13输入CSP平台登录地址
               add_data.get_excel(17, 5), # 14输入CSP平台功能介绍
               add_data.get_excel(18, 5), # 15上传新增的CSP的平台功能介绍附件
               add_data.get_excel(21, 5), # 16输入法人姓名
               add_data.get_excel(22, 5), # 17输入法人身份证号
               add_data.get_excel(23, 5), # 18上传法人身份证正面
               add_data.get_excel(24, 5), # 19上传法人身份证反面
               add_data.get_excel(25, 5), # 20输入法人邮箱
               add_data.get_excel(26, 5), # 21输入注册资金
               add_data.get_excel(27, 5), # 22处理注册地下拉框
               add_data.get_excel(28, 5), # 23输入注册地址
               (add_data.get_excel(2,5)+'5'),  #24
               add_data.get_excel(65,5),  #25csp草稿文件
               add_data.get_excel(67,5),  #26草稿csp名称
               ]
    add_legal_value = [add_data.get_excel(29, 5),  # 0输入年检度
                 add_data.get_excel(30, 5),  # 1输入经营范围
                 add_data.get_excel(31, 5),  # 2处理是否三证合一下拉框
                 add_data.get_excel(32, 5),  # 3输入统一社会信用代码
                 add_data.get_excel(33, 5),  # 4输入注册号
                 add_data.get_excel(39, 5),  # 5上传营业执照附件
                 add_data.get_excel(40, 5),  # 6输入税务类型
                 add_data.get_excel(41, 5),  # 7输入税务登记号
                 add_data.get_excel(42, 5),  # 8上传税务登记证附件
                 add_data.get_excel(43, 5),  # 9输入组织机构代码
                 add_data.get_excel(44, 5),  # 10上传组织机构附件
                 add_data.get_excel(45, 5),  # 11输入银行账户类型
                 add_data.get_excel(46, 5),  # 12输入开户名
                 add_data.get_excel(47, 5),  # 13输入开户银行
                 add_data.get_excel(48, 5),  # 14输入银行账号
                 add_data.get_excel(51, 5),  # 15上传开户许可证附件
                 add_data.get_excel(52, 5),  # 16输入合同编号
                 add_data.get_excel(53, 5),  # 17输入合同名称
                 add_data.get_excel(58, 5),  # 18上传合同附件
                 add_data.get_excel(60, 5),  # 19点击选择文件
                 (add_data.get_excel(2,5)+'2'),  #20文件导入新增的csp名称
                 ]
    check=[Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=3).read_column(2),
           Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=3).read_column(4),
           Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=3).read_column(5),
           ]
    check_value = [check_data.get_excel(6,5),  # 0选择CSP类型
             check_data.get_excel(7,5),  # 1选择CSP状态查询
             check_data.get_excel(8,5),  # 2选择CSP所属省份
             check_data.get_excel(9,5),  # 3选择的审核类型
             check_data.get_excel(15,5), # 4输入审核通过原因
             check_data.get_excel(17,5), # 5输入审核不通过原因
             check_data.get_excel(20,5), # 6审核结果
                   ]
    update=[Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=2).read_column(2),
            Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=2).read_column(4),
            Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=2).read_column(5),
            ]
    update_value = [update_data.get_excel(2, 5),  # 0变更客户类型
              update_data.get_excel(3, 5),  # 1变更csp类型
              update_data.get_excel(8, 5),  # 2手动输入token
              ]
    ground=[Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=4).read_column(2),
            Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=4).read_column(4),
            Write_Excel(filepath=test_data+r'\test_csp_data.xlsx',number=4).read_column(5),
            ]
    groundingdata = grounding_data.get_excel(15,5)


    other_add_csp =add_data.get_excel(62,5) # 文件导入的csp名称
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
    updatecsp='测试专用'

    def intoform(self):
        """
        进入csp管理查询内置表单
        :return:
        """
        csp_log.csp_log.info(f'进入csp管理内置表单-------开始{self.search[0][1]}')
        self.click_element(self.search[1][1], self.search[2][1])
        csp_log.csp_log.info(f'进入csp管理内置表单-------开始{self.search[0][2]}')
        self.click_element(self.search[1][2], self.search[2][2])
        self.handleform(0)

    def find_csp_data(self,name=add_value[0],csp_type=add_value[2],adress=search_value[2]):
        """
        管理csp二级菜单查询出csp数据
        :param name: csp名称
        :param csp_type: csp类型默认为新建的csp类型即“集团csp”
        :param adress:csp所属省份
        :return:
        """

        self.intoform()
        csp_log.csp_log.info(f'csp管理查询页面-----开始{self.search[0][3]}')
        self.input_value(self.search[1][3], self.search[2][3], name)  # 输入CSP名称查询
        self.wait(0.5)
        csp_log.csp_log.info(f'csp管理查询页面-----开始{self.search[0][5]}')
        self.handle_select(self.search[1][5], self.search[2][5],csp_type)  # 选择csp类型
        self.wait(0.5)
        csp_log.csp_log.info(f'csp管理查询页面-----开始{self.search[0][7]}')
        self.handle_select(self.search[1][7], self.search[2][7], adress)  # 选择csp所属省份
        csp_log.csp_log.info(f'csp管理查询页面-----开始{self.search[0][8]}')
        self.click_element(self.search[1][8], self.search[2][8])  # 点击查询按钮
        self.wait(0.5)

    def look_csp_data(self):
        """
        查看csp数据
        :return:
        """
        self.wait(1)
        csp_log.csp_log.info(f'csp管理查询页面---------开始{self.search[0][9]}')
        self.click_element(self.search[1][9], self.search[2][9])  # 点击查看按钮
        self.wait(1)


    def update_csp(self,value,customer=update_value[0],csp=update_value[1]):
        """
        变更csp信息
        :param value:代表变更csp的客户类型、2 代表变更csp类型 3 代表变更csp的Token值 ，4 代表变更csp的接入密匙
        :param customer:
        :param csp:
        :return:
        """
        csp_log.csp_log.info(f'csp查看页面----------开始{self.update[0][1]}')
        self.click_element(self.update[1][1], self.update[2][1])  # 点击编辑按钮进入编辑页面
        self.wait(2)
        if value == '1':  # 变更客户类型
            self.handle_select(self.update[1][2], self.update[2][2],customer)
            csp_log.csp_log.info(f'开始{self.update[0][2]}')
            self.click_element(self.update[1][4], self.update[2][4])  # 提交变更审核
            csp_log.csp_log.info(f'开始{self.update[0][4]}')
            self.wait(2)
            self.F5()


        elif value == '2':  # 变更csp类型
            self.handle_select(self.update[1][3], self.update[2][3],csp)
            csp_log.csp_log.info(f'开始{self.update[0][3]}')
            self.click_element(self.update[1][4], self.update[2][4])  # 提交变更审核
            csp_log.csp_log.info(f'开始{self.update[0][4]}')
            self.wait(2)
            self.F5()


        elif value == '3':  # 变更TOken值
            self.wait(1)
            self.click_element(self.update[1][7], self.update[2][7])  # 点击手动输入
            csp_log.csp_log.info(f'开始{self.update[0][7]}')
            self.wait(1)
            self.input_value(self.update[1][8], self.update[2][8],self.update_value[2] + self.random_number())  # 输入变更的token值
            csp_log.csp_log.info(f'开始{self.update[0][8]}')
            self.wait(2)
            self.click_element(self.update[1][4], self.update[2][4])  # 提交变更审核
            self.wait(2)
            self.F5()


        elif value == '4':  # 变更接入密匙
            self.wait(1)
            self.click_element(self.update[1][9], self.update[2][9])
            csp_log.csp_log.info(f'开始{self.update[0][9]}')
            self.wait(2)
            self.click_element(self.update[1][4], self.update[2][4])  # 提交变更审核
            self.wait(2)
            self.F5()

    def new_csp(self, name=add_value[0]):
        """
        新建 csp
        :return:
        """

        self.intoform()
        try:
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][1]}')
            self.click_element(self.add[1][1], self.add[2][1])  # 点击新增CSP按钮
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][2]}')
            self.input_value(self.add[1][2], self.add[2][2],test_value=name)  # 输入新增的CSP名称
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][3]}')
            self.handle_select(self.add[1][3], self.add[2][3],self.add_value[1])  # 选择新增的CSP客户类型
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][4]}')
            self.handle_select(self.add[1][4], self.add[2][4], self.add_value[2])  # 选择csp类型
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][5]}')
            self.handle_select(self.add[1][5], self.add[2][5], self.add_value[3])  # 选择csp归属省份
            self.wait(1)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][6]}')
            self.handle_select(self.add[1][6], self.add[2][6], self.add_value[4])  # 选择csp归属地市\
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][7]}')
            self.input_value(self.add[1][7], self.add[2][7], self.add_value[5])  # 输入新增的CSP联系人
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][8]}')
            self.input_value(self.add[1][8], self.add[2][8], self.add_value[6])  # 输入新增的CSP联系电话
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][9]}')
            self.input_value(self.add[1][9], self.add[2][9], self.add_value[7])  # 输入新增的CSP联系人身份证号
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][10]}')
            self.input_value(self.add[1][10], self.add[2][10], self.add_value[8])  # 输入新增的CSP联系人邮箱
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][11]}')
            self.upload_file(self.add[1][11], self.add[2][11], self.add_value[9])  # 上传新增的CSP的经办人身份证正面
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][12]}')
            self.upload_file(self.add[1][12], self.add[2][12], self.add_value[10])  # 上传新增的CSP的经办人身份证反面
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][13]}')
            self.input_value(self.add[1][13], self.add[2][13], self.add_value[11])  # 输入IP地址
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][14]}')
            self.input_value(self.add[1][14], self.add[2][14], self.add_value[12])  # 输入CSP回调根目录地址
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][15]}')
            self.click_element(self.add[1][15], self.add[2][15])  # 点击系统自动生成token
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][16]}')
            self.input_value(self.add[1][16], self.add[2][16], self.add_value[13])  # 输入CSP平台登录地址
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][17]}')
            self.input_value(self.add[1][17], self.add[2][17], self.add_value[14])  # 输入CSP平台功能介绍
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][18]}')
            self.upload_file(self.add[1][18], self.add[2][18], self.add_value[15])  # 上传新增的CSP的平台功能介绍附件
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][19]}')
            self.input_value(self.add[1][19], self.add[2][19], self.random_number())  # 输入BIZID
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][20]}')
            self.input_value(self.add[1][20], self.add[2][20], self.random_number())  # 输入接入码
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][21]}')
            self.input_value(self.add[1][21], self.add[2][21], self.add_value[16])  # 输入法人姓名
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][22]}')
            self.input_value(self.add[1][22], self.add[2][22], self.add_value[17])  # 输入法人身份证号
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][23]}')
            self.upload_file(self.add[1][23], self.add[2][23], self.add_value[18])  # 上传法人身份证正面
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][24]}')
            self.upload_file(self.add[1][24], self.add[2][24], self.add_value[19])  # 上传法人身份证反面
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][25]}')
            self.input_value(self.add[1][25], self.add[2][25], self.add_value[20])  # 输入法人邮箱
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][26]}')
            self.input_value(self.add[1][26], self.add[2][26], self.random_number())  # 输入注册资金
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][27]}')
            self.handle_select(self.add[1][27], self.add[2][27], self.add_value[22])  # 处理注册地下拉框
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][28]}')
            self.input_value(self.add[1][28], self.add[2][28], self.add_value[23])  # 输入注册地址

            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][29]}')
            self.input_value(self.add[1][29], self.add[2][29],self.add_legal_value[0])  # 输入年检度
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][30]}')
            self.input_value(self.add[1][30], self.add[2][30], self.add_legal_value[1])  # 输入经营范围
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][31]}')
            self.handle_select(self.add[1][31], self.add[2][31], self.add_legal_value[2])  # 处理是否三证合一下拉框
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][32]}')
            self.input_value(self.add[1][32], self.add[2][32],
                             self.random_number() + self.random_number())  # 输入统一社会信用代码
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][33]}')
            self.input_value(self.add[1][33], self.add[2][33],
                             self.random_number() + self.random_number())  # 输入注册号
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][34]}')
            self.jsp(self.add[2][34])
            self.wait(0.5)
            self.jsp(self.add[2][35])  # 输入营业开始时间
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][36]}')
            self.click_element(self.add[1][36], self.add[2][36])  # 选择营业结束时间为长期
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][37]}')
            self.jsp(self.add[2][37])
            self.wait(0.5)
            self.jsp(self.add[2][38])  # 输入发证时间
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][39]}')
            self.upload_file(self.add[1][39], self.add[2][39],self.add_legal_value[5])  # 上传营业执照附件
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][40]}')
            self.input_value(self.add[1][40], self.add[2][40], self.add_legal_value[6])  # 输入税务类型
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][41]}')
            self.input_value(self.add[1][41], self.add[2][41],
                             self.random_number() + self.random_number())  # 输入税务登记号
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][42]}')
            self.upload_file(self.add[1][42], self.add[2][42], self.add_legal_value[8])  # 上传税务登记证附件
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][43]}')
            self.input_value(self.add[1][43], self.add[2][43], self.random_number())  # 输入组织机构代码
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][44]}')
            self.upload_file(self.add[1][44], self.add[2][44], self.add_legal_value[10])  # 上传组织机构附件
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][45]}')
            self.input_value(self.add[1][45], self.add[2][45],self.add_legal_value[11])  # 输入银行账户类型
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][46]}')
            self.input_value(self.add[1][46], self.add[2][46], self.add_legal_value[12])  # 输入开户名
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][47]}')
            self.input_value(self.add[1][47], self.add[2][47], self.add_legal_value[13])  # 输入开户银行
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][48]}')
            self.input_value(self.add[1][48], self.add[2][48],
                             self.add_legal_value[14] + self.random_number())  # 输入银行账号
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][49]}')
            self.jsp(self.add[2][49])
            self.wait(0.5)
            self.jsp(self.add[2][50])  # 输入开户时间
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][51]}')
            self.upload_file(self.add[1][51], self.add[2][51],self.add_legal_value[15])  # 上传开户许可证附件
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][52]}')
            self.input_value(self.add[1][52], self.add[2][52], self.random_number())  # 输入合同编号
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][53]}')
            self.input_value(self.add[1][53], self.add[2][53], self.add_legal_value[7])  # 输入合同名称
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][54]}')
            self.jsp(self.add[2][54])
            self.wait(0.5)
            self.jsp(self.add[2][55])  # 输入合同开始时间
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][56]}')
            self.jsp(self.add[2][56])
            self.wait(0.5)
            self.jsp(self.add[2][57])  # 输入合同结束时间
            self.wait(2)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][58]}')
            self.upload_file(self.add[1][58], self.add[2][58],self.add_legal_value[18])  # 上传合同附件
            self.wait(1)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][59]}')
            self.click_element(self.add[1][59], self.add[2][59])  # 点击提交审核
            self.wait(1)
        except Exception:
            csp_log.csp_log.exception(f'新建{self.add_value[0]}失败')
            raise
        else:
            write_text.Text_action(Conf.notebook + r'\notebook.txt').write_file(value=f'{self.nowtime}-----{name}')
        finally:
                self.F5()


    def intocheck(self, way:bool):
        """
        进入审核csp内置表单
        :param way:
        :return:
        """
        self.click_element(self.search[1][1], self.search[2][1])
        csp_log.csp_log.info(f'进入审核内置表单-----开始{self.search[0][1]}')
        self.click_element(self.check[1][1], self.check[2][1])
        csp_log.csp_log.info(f'进入审核内置表单-----开始{self.check[0][1]}')
        self.handleform(0)
        self.wait(2)

        # 判断页面是否存在身份验证
        if way ==True:

            if self.isElementExist((By.XPATH,self.check[2][2])):
                csp_log.csp_log.info(f'审核身份验证-------开始{self.check[0][2]}')
                self.wait(25)
                self.click_element(self.check[1][3], self.check[2][3])
                csp_log.csp_log.info(f'审核身份验证------开始{self.check[0][3]}')
            else:
                csp_log.csp_log.info('无需身份验证')
        else:
            csp_log.csp_log.info(f'进入chatbot审核二级表单')

    def find_check_csp(self,cspname=add_value[0],way='0',check_csp_type=add_value[2],check_way=check_value[3],check_result=check_value[6]):
        """
        csp审核二级菜单查询待审核或已审核的csp
        :param cspname: 查询的csp名称
        :param way: 选择待审核或者已审核
        :param check_csp_type:查询的csp类型 默认集团csp
        :param check_way: 查询的csp审核类型 默认信息创建
        :param check_result: csp审核结果   默认审核通过
        :return:
        """
        if way == '0':
            csp_log.csp_log.info(f'默认点击待审核')
        else:
            csp_log.csp_log.info(f'审核页面----开始{self.check[0][11]}')
            self.click_element(self.check[1][11], self.check[2][11])  # 点击已审核
            csp_log.csp_log.info(f'审核页面-----开始{self.check[0][20]}')
            self.wait(2)
            self.handle_select(self.check[1][20], self.check[2][20],check_result)  # 选择审核结果
            self.wait(0.5)
        self.wait(1)
        csp_log.csp_log.info(f'审核页面-----开始{self.check[0][4]}')
        self.input_value(self.check[1][4], self.check[2][4], cspname)  # 输入查询条件
        self.wait(1)
        csp_log.csp_log.info(f'审核页面------开始{self.check[0][6]}')
        self.wait(1)
        self.handle_select(self.check[1][6], self.check[2][6],check_csp_type)  # 选择csp类型
        self.wait(1)
        csp_log.csp_log.info(f'审核页面------开始{self.check[0][9]}')
        self.wait(1)
        self.handle_select(self.check[1][9],self.check[2][9],check_way)          #选择审核类型
        csp_log.csp_log.info(f'审核页面-------开始{self.check[0][12]}')
        self.wait(1)
        self.click_element(self.check[1][12], self.check[2][12])  # 点击查询
        self.wait(1)

    def look_check_csp(self):
        """
        查看待审核的数据
        :return:
        """
        csp_log.csp_log.info(f'审核页面-----开始{self.check[0][13]}-----进入查看页面')
        self.click_element(self.check[1][13], self.check[2][13])  # 点击查看按钮
        self.wait(0.5)
    def look_checked_csp(self):
        """
        点击查看已经审核的csp数据
        :return:
        """
        csp_log.csp_log.info(f'审核页面 ------开始{self.check[0][19]}')
        self.click_element(self.check[1][19], self.check[2][19])
        self.wait(0.5)
    def starting_check(self, result='0'):
        """
        开始审核
        :param result:
        :return:
        """
        csp_log.csp_log.info(f'审核页面----开始{self.check[0][14]}')
        self.click_element(self.check[1][14], self.check[2][14])  # 点击审核按钮
        self.wait(2)
        if result == '0':  # 审核通过
            csp_log.csp_log.info(f'进入审核页面------------开始{self.check[0][15]}')
            self.input_value(self.check[1][15], self.check[2][15], self.check_value[4])  # 输入审核通过原因

        else:
            csp_log.csp_log.info(f'进入审核页面------------开始{self.check[0][16]}')
            self.click_element(self.check[1][16], self.check[2][16])  # 点击审核不通过
            csp_log.csp_log.info(f'进入审核页面------------开始{self.check[0][17]}')
            self.input_value(self.check[1][17], self.check[2][17],self.check_value[5])  # 输入审核不通过原因
        csp_log.csp_log.info(f'进入审核页面------------开始{self.check[0][18]}')
        self.click_element(self.check[1][18], self.check[2][18])  # 点击确认审核结果
        self.wait(0.5)
        self.F5()

    def look_update(self, text):
        """
        查看变更的内容
        :param text:
        :return:
        """

        if text == '1':  # 查看token变更内容
            self.wait(1)
            csp_log.csp_log.info(f'csp查看页面----------开始{self.update[0][11]}')
            token_value = self.isElementExist((By.LINK_TEXT, self.update[2][11]))

            return token_value

        elif text == '2':  # 查看接入密匙前后变更内容
            self.wait(1)
            csp_log.csp_log.info(f'csp查看页面----------开始{self.update[0][10]}')
            code_value = self.isElementExist((By.LINK_TEXT, self.update[2][10]))
            return code_value

        elif text == '3':  # 点击查看客户类型变更前后内容
            self.wait(1)
            csp_log.csp_log.info(f'csp查看页面----------开始{self.update[0][12]}')
            self.isElementExist((By.LINK_TEXT, self.update[2][12]))

        elif text == '4':  # 点击查看csp类型变更前后内容
            self.wait(1)
            csp_log.csp_log.info(f'csp查看页面----------开始{self.update[0][13]}')
            self.isElementExist((By.LINK_TEXT, self.update[2][13]))

    def grounding_on(self):
        """
        csp管理二级菜单查询出数据点击查看进入页面进行上架操作
        :return:
        """
        self.wait(1)
        csp_log.csp_log.info(f'csp查看页面----------开始{self.search[0][10]}')
        self.click_element(self.search[1][10], self.search[2][10])  # 点击上架该csp
        self.wait(0.5)
        csp_log.csp_log.info(f'csp查看页面----------开始{self.search[0][11]}')
        self.click_element(self.search[1][11], self.search[2][11])  # 点击确认上架
        self.wait(1)
        csp_log.csp_log.info(f'csp查看页面----------开始{self.search[0][12]}')
        self.upload_file(self.search[1][12], self.search[2][12],self.search_value[3])  # 上传报告
        self.wait(2)
        csp_log.csp_log.info(f'csp查看页面----------开始{self.search[0][13]}')
        self.click_element(self.search[1][13], self.search[2][13])  # 点击确认提交审核按钮
        self.wait(0.5)
        self.F5()

    def grounding_off(self):
        """
        csp管理二级菜单查询出数据点击查看进入页面操作下架
        :return:
        """
        csp_log.csp_log.info(f'csp查看页面--------开始{self.ground[0][12]}')
        self.click_element(self.ground[1][12], self.ground[2][12])  # 点击下架按钮
        self.wait(1)
        csp_log.csp_log.info(f'csp查看页面--------开始{self.ground[0][13]}')
        self.click_element(self.ground[1][13], self.ground[2][13])  # 点击确定下架按钮
        self.wait(2)
        self.F5()

    def grounding_on_again(self):
        """
        csp管理二级菜单查询存在过上架记录且当前csp状态为已下架的csp数据，查看页面操作再次上架申请
        :return:
        """
        csp_log.csp_log.info(f'csp查看页面--------开始{self.ground[0][14]}')
        self.click_element(self.ground[1][14], self.ground[2][14])  # 查看页面点击上架申请记录的编辑按钮
        #csp_log.csp_log.info(f'csp查看页面--------开始{self.ground[0][15]}')
        #self.upload_file(self.ground[1][15], self.ground[2][15],self.groundingdata)  # 上传附件
        csp_log.csp_log.info(f'csp查看页面--------开始{self.ground[0][16]}')
        self.wait(1)
        self.click_element(self.ground[1][16], self.ground[2][16])  # 点击提交审核
        self.wait(1)
        self.F5()

    def grouding_check_form(self, grounding_way:bool):
        """
        进入上架审核二级菜单
        :param grounding_way:
        :return:
        """
        self.wait(2)
        csp_log.csp_log.info(f'进入上架审核内置表单----------开始{self.search[0][1]}')
        self.click_element(self.search[1][1], self.search[2][1])
        csp_log.csp_log.info(f'进入上架审核内置表单----------开始{self.ground[0][1]}')
        self.click_element(self.ground[1][1],self.ground[2][1])
        self.handleform(0)

        if grounding_way ==True:
               csp_log.csp_log.info(f'进入上架审核内置表单---------开始{self.ground[0][2]}')
               self.click_element(self.ground[1][2], self.ground[2][2])
               self.wait(25)
               csp_log.csp_log.info(f'进入上架审核内置表单---------开始{self.ground[0][3]}')
               self.click_element(self.ground[1][3], self.ground[2][3])
               self.wait(2)
        else:
               csp_log.csp_log.info(f'进入chatbot审核二级表单')

    def find_grounding_data(self, grounding_name=add_value[0],gronding_csp_type=add_value[2]):
        """
        查询出待审核的上架申请数据
        :param grounding_name:
        :return:
        """
        self.wait(1)
        csp_log.csp_log.info(f'上架审核查询页面-------------开始{self.ground[0][4]}')
        self.click_element(self.ground[1][4], self.ground[2][4])  # 点击待审核
        self.wait(1)
        csp_log.csp_log.info(f'上架审核查询页面-------------开始{self.ground[0][5]}')
        self.input_value(self.ground[1][5], self.ground[2][5],grounding_name)  # 输入查询条件
        self.wait(0.5)
        csp_log.csp_log.info(f'上架审核查询页面-------------开始{self.ground[0][6]}')
        self.handle_select(self.ground[1][6], self.ground[2][6],gronding_csp_type)  # 选择csp类型
        self.wait(1)
        csp_log.csp_log.info(f'上架审核查询页面-------------开始{self.ground[0][7]}')
        self.click_element(self.ground[1][7], self.ground[2][7])  # 点击查询按钮
        self.wait(0.5)

    def check_grounding(self, result='1'):
        """
        审核页面，开始审核上架申请
        :param result:
        :return:
        """
        self.wait(1)
        csp_log.csp_log.info(f'上架审核查询页面-------------开始{self.ground[0][8]}')
        self.click_element(self.ground[1][8], self.ground[2][8])  # 点击审核按钮
        if result == '1':
            # 审核通过
            csp_log.csp_log.info(f'上架审核页面-------------开始{self.ground[0][9]}')
            self.input_value(self.ground[1][9], self.ground[2][9], self.random_number())

        elif result == '0':
            # 审核不同过
            csp_log.csp_log.info(f'上架审核页面------------开始{self.ground[0][11]}')
            self.click_element(self.ground[1][11], self.ground[2][11])  # 点击审核不通过
            self.wait(1)
            csp_log.csp_log.info(f'上架审核页面------------开始{self.ground[0][9]}')
            self.input_value(self.ground[1][9], self.ground[2][9], self.random_number())
        csp_log.csp_log.info(f'上架审核页面------------开始{self.ground[0][10]}')
        self.wait(1)
        self.click_element(self.ground[1][10], self.ground[2][10])  # 点击确认审核
        self.wait(0.5)
        self.F5()

    def look_gronding(self,status:bool,grounded_csp=add_value[0],result=search_value[1]):
        """
        查询已经上架或者下架的csp
        :param result:
        :param more: 查询出数据后更多的操作默认不点击查看
        :param status:
        :return:
        """

        self.intoform()  # 进入csp管理内置表单
        if status==True:
            csp_log.csp_log.info(f'csp管理页面查询------开始{self.search[0][6]}')
            self.handle_select(self.search[1][6], self.search[2][6],result)  # 选择csp状态
        else:
            csp_log.csp_log.info(f'无需选择csp状态')


        csp_log.csp_log.info(f'csp管理页面查询------开始{self.search[0][3]}')
        self.wait(1)
        self.input_value(self.search[1][3], self.search[2][3],grounded_csp)  # 输入csp名称
        csp_log.csp_log.info(f'csp管理页面查询------开始{self.search[0][8]}')
        self.wait(1)
        self.click_element(self.search[1][8],self.search[2][8])
        self.wait(0.5)

    def get_assert_text(self, text=add_value[0]):
        """
        返回查询节点csp名称文本值
        :param text:
        :return:
        """
        value = f'<td>{text}</td>'
        return value
    def get_assert_look_text(self,element_text):
        """

        :param element_text:
        :return:
        """
        value1 = f'<div>{element_text}</div>'
        return value1


    def other_add(self,add_name=other_add_csp,add_file=add_legal_value[19]):
        """

        :return:
        """
        self.intoform()
        try:
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][1]}')
            self.click_element(self.add[1][1],self.add[2][1])
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][60]}')
            self.upload_file(self.add[1][60], self.add[2][60],add_file)  # 上传文件
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][61]}')
            self.click_element(self.add[1][61], self.add[2][61])  # 点击开始上传
            self.wait(2)
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][2]}')
            self.input_value(self.add[1][2], self.add[2][2],add_name)  # 输入csp名称
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][11]}')
            self.upload_file(self.add[1][11], self.add[2][11],self.add_value[9])  # 上传新增的CSP的经办人身份证正面
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][12]}')
            self.wait(0.5)
            self.upload_file(self.add[1][12], self.add[2][12], self.add_value[10])  # 上传新增的CSP的经办人身份证反面
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][15]}')
            self.click_element(self.add[1][15], self.add[2][15])  # 点击系统自动生成token
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][17]}')
            self.input_value(self.add[1][17], self.add[2][17], self.add_value[14])  # 输入CSP平台功能介绍
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面--------开始{self.add[0][18]}')
            self.upload_file(self.add[1][18], self.add[2][18], self.add_value[15])  # 上传新增的CSP的平台功能介绍附件
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][20]}')
            self.input_value(self.add[1][20], self.add[2][20], self.random_number())  # 输入接入码
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][23]}')
            self.wait(0.5)
            self.upload_file(self.add[1][23], self.add[2][23], self.add_value[18])  # 上传法人身份证正面
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][24]}')
            self.wait(0.5)
            self.upload_file(self.add[1][24], self.add[2][24], self.add_value[19])  # 上传法人身份证反面
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][39]}')
            self.wait(0.5)
            self.upload_file(self.add[1][39], self.add[2][39], self.add_legal_value[5])  # 上传营业执照附件
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][42]}')
            self.upload_file(self.add[1][42], self.add[2][42], self.add_legal_value[8])  # 上传税务登记证附件
            self.wait(0.5)
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][44]}')
            self.upload_file(self.add[1][44], self.add[2][44], self.add_legal_value[10])  # 上传组织机构附件
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][51]}')
            self.wait(0.5)
            self.upload_file(self.add[1][51], self.add[2][51], self.add_legal_value[15])  # 上传开户许可证附件
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][58]}')
            self.wait(0.5)
            self.upload_file(self.add[1][58], self.add[2][58], self.add_legal_value[18])  # 上传合同附件
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][59]}')
            self.wait(0.5)
            self.click_element(self.add[1][59], self.add[2][59])  # 点击提交审核)
            self.wait(0.5)
        except Exception:
            csp_log.csp_log.exception(f'新增csp{self.other_add_csp}失败')
            raise
        else:
            csp_log.csp_log.exception(f'新增csp{self.other_add_csp}成功')
            write_text.Text_action(Conf.notebook + r'\notebook.txt').write_file(value=f'{self.nowtime}-----{self.other_add_csp}')
        finally:
            self.F5()

    def otheraddcsp(self,way:bool,add_csp_name=add_value[26],add_csp_file=add_value[25]):
        """

        :param way:
        :param add_csp_name:
        :param add_csp_file:
        :return:
        """
        self.intoform()
        if way==False:
            csp_log.csp_log.info(f'csp新增页面------------开始{self.add[0][1]}')
            self.click_element(self.add[1][1], self.add[2][1])  # 点击新增CSP按钮
            self.wait(1)
            self.other_add()
        elif way==True:
            csp_log.csp_log.info(f'新增草稿-------开始{self.add[0][63]}')
            self.click_element(self.add[1][63],self.add[2][63])   #点击csp草稿
            self.wait(0.5)
            csp_log.csp_log.info(f'新增草稿--------开始{self.add[0][64]}')
            self.click_element(self.add[1][64],self.add[2][64])
            self.wait(0.5)
            self.other_add(add_name=add_csp_name,add_file=add_csp_file)

    def find_othercsp(self,csp=add_value[26],type=add_value[2]):
        """

        :param csp:
        :param type:
        :return:
        """
        csp_log.csp_log.info(f'查询csp草稿------开始{self.search[0][3]}')
        self.input_value(self.search[1][3],self.search[2][3],csp)
        self.wait(0.5)
        csp_log.csp_log.info(f'查询csp草稿------开始{self.search[0][5]}')
        self.input_value(self.search[1][5],self.search[2][5],type)
        self.wait(0.5)
        csp_log.csp_log.info(f'查询csp草稿------开始{self.search[0][8]}')
        self.click_element(self.search[1][8],self.search[2][8])
        self.wait(1)





    def assert_find(self,findname,assert_text,findtype=add_value[2],findadress=search_value[2]):
        """
        查询断言
        :param findname:
        :param assert_text:
        :param findtype
        :param findadress
        :return:
        """
        value = assert_text
        self.find_csp_data(name=findname,csp_type=findtype,adress=findadress)
        code = self.getpagecode()
        if value in code:
            return True
        else:
            return False
    def refresh(self):
        """
        还原csp客户类型和csp类型
        :return:
        """
        csp_log.csp_log.info(f'csp查看页面----------开始{self.update[0][1]}')
        self.click_element(self.update[1][1], self.update[2][1])  # 点击编辑按钮进入编辑页面
        self.wait(0.5)
        self.handle_select(self.update[1][2],self.update[2][2],self.add_value[1])
        csp_log.csp_log.info(f'开始{self.update[0][2]}')
        self.wait(0.5)
        self.handle_select(self.update[1][3],self.update[2][3],self.add_value[2])
        csp_log.csp_log.info(f'开始{self.update[0][3]}')
        self.wait(0.5)
        self.click_element(self.update[1][4], self.update[2][4])  # 提交变更审核
        csp_log.csp_log.info(f'开始{self.update[0][4]}')
        self.wait(0.5)
        self.F5()




if __name__ == '__main__':
    pass


