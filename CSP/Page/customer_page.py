from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *
custmoer_log=Log(__name__,file=logging.INFO,cmd=logging.INFO)
add_data=ReadExcel(filepath=test_data+r'\test_customer_data.xlsx',sheetname="add")
search_data=ReadExcel(filepath=test_data+r'\test_customer_data.xlsx',sheetname="search")
update_data = ReadExcel(filepath=test_data+r'\test_customer_data.xlsx',sheetname="update")
check_data = ReadExcel(filepath=test_data+r'\test_customer_data.xlsx',sheetname="check")

class CustmoerPage(BasePage):


    add = [(add_data.get_excel(1,3),add_data.get_excel(1,4)),  #0点击“新增客户”按钮
           (add_data.get_excel(2,3),add_data.get_excel(2,4),add_data.get_excel(2,5)), #1输入新增的客户名称
           (add_data.get_excel(3,3),add_data.get_excel(3,4),add_data.get_excel(3,5)), #2操作选择所属csp下拉框
           (add_data.get_excel(4,3),add_data.get_excel(4,4),add_data.get_excel(4,5)), #3上传企业logo
           (add_data.get_excel(5,3),add_data.get_excel(5,4),add_data.get_excel(5,5)), #4上传营业执照
           (add_data.get_excel(6,3),add_data.get_excel(6,4),add_data.get_excel(6,5)), #5输入企业介绍
           (add_data.get_excel(7,3),add_data.get_excel(7,4),add_data.get_excel(7,5)), #6输入企业所在地
           (add_data.get_excel(8,3),add_data.get_excel(8,4),add_data.get_excel(8,5)), #7处理行业类型下拉框
           (add_data.get_excel(9,3),add_data.get_excel(9,4),add_data.get_excel(9,5)), #8处理客户等级下拉框
           (add_data.get_excel(10,3),add_data.get_excel(10,4),add_data.get_excel(10,5)), #9输入企业法人
           (add_data.get_excel(11,3),add_data.get_excel(11,4),add_data.get_excel(11,5)), #10输入企业法人身份证号
           (add_data.get_excel(12,3),add_data.get_excel(12,4),add_data.get_excel(12,5)), #11上传企业法人身份证正面
           (add_data.get_excel(13,3),add_data.get_excel(13, 4),add_data.get_excel(13, 5)), #12上传企业法人身份证反面
           (add_data.get_excel(14,3),add_data.get_excel(14, 4),add_data.get_excel(14, 5)), #13输入客户联系人姓名
           (add_data.get_excel(15,3),add_data.get_excel(15, 4),add_data.get_excel(15, 5)), #14输入客户联系人电话
           (add_data.get_excel(16,3),add_data.get_excel(16, 4),add_data.get_excel(16, 5)),#15输入客户联系人邮箱
           (add_data.get_excel(17,3),add_data.get_excel(17,4),add_data.get_excel(17,5)),  #16输入客户联系人身份证号
           (add_data.get_excel(18,3), add_data.get_excel(18,4),add_data.get_excel(18,5)), #17上传客户联系人身份证正面
           (add_data.get_excel(19,3),add_data.get_excel(19,4),add_data.get_excel(19,5)), #18上传客户联系人身份证反面
           (add_data.get_excel(20,3),add_data.get_excel(20,4)), #19输入合同编号
           (add_data.get_excel(21,3),add_data.get_excel(21,4),add_data.get_excel(21,5)),  #20输入合同名称
           (add_data.get_excel(22,3),add_data.get_excel(22,4),add_data.get_excel(22,5)),  #21输入合同生效日期
           (add_data.get_excel(23,3),add_data.get_excel(23,4),add_data.get_excel(23,5)),  #22输入合同失效日期
           (add_data.get_excel(24,3),add_data.get_excel(24,4)),  #23点击是否续约为是
           (add_data.get_excel(25,3),add_data.get_excel(25,4),add_data.get_excel(25,5)),  #24输入合同续约日期
           (add_data.get_excel(26,3),add_data.get_excel(26,4),add_data.get_excel(26,5)),  #25上传合同附件
           (add_data.get_excel(27,3),add_data.get_excel(27,4)),  #26点击确认新建客户按钮
           (add_data.get_excel(28,3),add_data.get_excel(28,4),add_data.get_excel(28,5)),  #27输入办公电话
           add_data.get_excel(2,5)+'1',  #28新增另一个客户名称
           ]

    search = [(search_data.get_excel(1,3),search_data.get_excel(1,4)), #0点击客户管理一级菜单
              (search_data.get_excel(2,3),search_data.get_excel(2,4)), #1点击客户管理二级菜单
              (search_data.get_excel(3,3),search_data.get_excel(3,4),search_data.get_excel(3,5)), #2输入客户名称查询
              (search_data.get_excel(4,3),search_data.get_excel(4,4),search_data.get_excel(4,5)), #3输入客户编码查询
              (search_data.get_excel(5,3),search_data.get_excel(5,4),search_data.get_excel(5,5)), #4选择所属省份下拉框
              (search_data.get_excel(6,3),search_data.get_excel(6,4),search_data.get_excel(6,5)), #5选择客户类型下拉框
              (search_data.get_excel(7,3),search_data.get_excel(7,4)), #6点击确认查询按钮
              (search_data.get_excel(8,3),search_data.get_excel(8,4)),#7查询出数据点击查看按钮
              (search_data.get_excel(9,3),search_data.get_excel(9,4)), #8获取客户管理模块客户名称文本值
              (search_data.get_excel(10,3),search_data.get_excel(10,4)), #9获取客户信息查看页面客户类型文本值
              (search_data.get_excel(11,3),search_data.get_excel(11,4)), #10获取客户信息查看页面客户归属csp文本值
              (search_data.get_excel(12,3),search_data.get_excel(12,4)), #11点击注销客户按钮
              (search_data.get_excel(13,3),search_data.get_excel(13,4)), #12确认注销按钮
              (search_data.get_excel(14,3),search_data.get_excel(14,4)), #13获取查看客户数据页面客户编码
              ]

    check = [(check_data.get_excel(1,3),check_data.get_excel(1,4)),  #0点击客户审核二级菜单
             (check_data.get_excel(2,3),check_data.get_excel(2,4)),  #1点击CSP客户类型
             (check_data.get_excel(3,3),check_data.get_excel(3,4)),  #2点击集团客户类型
             (check_data.get_excel(4,3),check_data.get_excel(4,4)),  #3点击省公司客户类型
             (check_data.get_excel(5,3),check_data.get_excel(5,4)),  #4点击其他客户类型
             (check_data.get_excel(6,3),check_data.get_excel(6,4),check_data.get_excel(6,5)), #5输入客户名称查询审核数据
             (check_data.get_excel(7,3),check_data.get_excel(7,4),check_data.get_excel(7,5)), #6输入客户编码查询审核数据
             (check_data.get_excel(8,3),check_data.get_excel(8,4),check_data.get_excel(8,5)), #7选择所属省份查询审核数据
             (check_data.get_excel(9,3),check_data.get_excel(9,4),check_data.get_excel(9,5)), #8选择审核类型查询审核数据
             (check_data.get_excel(10,3),check_data.get_excel(10,4)),  #9选择归属csp
             (check_data.get_excel(11,3),check_data.get_excel(11,4)),  #10点击查询按钮
             (check_data.get_excel(12,3),check_data.get_excel(12,4)),  #11获取客户审核页面客户名称文本
             (check_data.get_excel(13,3),check_data.get_excel(13,4)),   #12点击审核按钮
             (check_data.get_excel(14,3),check_data.get_excel(14,4)),   #13选择审核通过
             (check_data.get_excel(15,3),check_data.get_excel(15,4)),   #14选择审核不通过
             (check_data.get_excel(16,3),check_data.get_excel(16,4),check_data.get_excel(16,5)), #15输入审核不通过原因
             (check_data.get_excel(17,3),check_data.get_excel(17,4)),   #16点击确定审核按钮
             (check_data.get_excel(18,3),check_data.get_excel(18,4)),   #17点击待审核
             (check_data.get_excel(19,3),check_data.get_excel(19,4)),   #18点击已审核
             (check_data.get_excel(20,3),check_data.get_excel(20,4)),   #19点击已审核客户查看按钮
             (check_data.get_excel(21,3),check_data.get_excel(21,4)),   #20点击获取身份验证码
             (check_data.get_excel(22,3),check_data.get_excel(22,4))]   #21点击确定按钮

    update_user=[(update_data.get_excel(1,3),update_data.get_excel(1,4)),  #0点击编辑按钮
                 (update_data.get_excel(2,3),update_data.get_excel(2,4),update_data.get_excel(2,5)), #1变更客户名称
                 (update_data.get_excel(3,3),update_data.get_excel(3,4)), #点击变更所属CSP
                 (update_data.get_excel(4,3),update_data.get_excel(4,4)), #点击选择中国电信10000
                 (update_data.get_excel(5,3),update_data.get_excel(5,4)), #点击确认变更按钮
                 ]





    def intoform(self):
        """
        进入客户管理二级菜单查询节点
        :return:
        """
        self.click_element(self.search[0][0],self.search[0][1])
        self.click_element(self.search[1][0],self.search[1][1])
        self.handleform(0)

    def find_name(self,customername=add[1][-1]):
        """
        按客户名称和客户类型查询数据
        :param customername:
        :return:
        """
        self.intoform()
        self.wait(2)
        self.input_value(self.search[2][0],self.search[2][1],customername)  #输入客户名称查询
        self.wait(2)
        self.handle_select(self.search[5][0],self.search[5][1],self.search[5][2])  # 选择客户类型
        self.wait(2)
        self.click_element(self.search[6][0],self.search[6][1])  #点击查询按钮
        self.wait(2)

    def get_user_text(self):
        """
        获取客户管理节点客户名称文本值
        :return:
        """
        try:
            value = self.get_text(self.search[8][0],self.search[8][1])    #获取客户名称文本值
        except Exception:
            custmoer_log.csp_log.exception(f'查询的客户不存在')
            return False
        else:
            custmoer_log.csp_log.info(f'查询到客户{self.add[1][-1]}')
            return value


    def look_user(self):
        """
        点击查看客户信息
        :return:
        """
        self.click_element(self.search[7][0],self.search[7][1])  #点击查看按钮
        self.wait(2)

    def into_view_page(self,data='0'):
        """
        进入查看数据页面
        :param data:
        :return:
        """
        self.find_name()
        if data=='0':
            return self.get_text(self.search[9][0],self.search[9][1])  #获取客户信息查看页面客户类型文本值
        elif data=='1':
            return self.get_text(self.search[10][0],self.search[10][1]) #获取客户信息查看页面客户归属csp文本值

    def delete_user(self):
        """
        注销客户
        :return:
        """
        self.look_user() #点击查看按钮
        code = self.get_text(self.search[13][0],self.search[13][1])

        self.click_element(self.search[11][0],self.search[11][1])  #点击注销按钮
        self.wait(2)
        self.click_element(self.search[12][0],self.search[12][1])  #点击确认注销按钮
        self.wait(3)
        self.F5()
        return code

    def add_customer(self,name=add[1][2]):
        """
        新增客户
        :param name: 新增的客户名称
        :return:
        """
        self.intoform()
        self.click_element(self.add[0][0],self.add[0][1])
        self.wait(2)
        self.input_value(self.add[1][0],self.add[1][1],name)  #输入客户名称
        self.wait(2)
        self.handle_select(self.add[2][0],self.add[2][1],self.add[2][2])   #操作选择所属csp下拉框
        self.wait(2)
        self.upload_file(self.add[3][0],self.add[3][1],self.add[3][2])   #上传企业logo
        self.wait(2)
        self.upload_file(self.add[4][0],self.add[4][1],self.add[4][2])   #上传营业执照
        self.wait(2)
        self.input_value(self.add[5][0],self.add[5][1],self.add[5][2])  #输入企业介绍
        self.wait(2)
        self.input_value(self.add[6][0],self.add[6][1],self.add[6][2])   #输入企业所在地
        self.wait(2)
        self.handle_select(self.add[7][0],self.add[7][1],self.add[7][2])   #处理行业类型下拉框
        self.wait(2)
        self.input_value(self.add[27][0],self.add[27][1],self.add[27][2])  #输入办公电话
        self.wait(2)
        self.handle_select(self.add[8][0],self.add[8][1],self.add[8][2])  #处理客户等级下拉框
        self.wait(2)
        self.input_value(self.add[9][0],self.add[9][1],self.add[9][2]) #输入企业法人
        self.wait(2)
        self.input_value(self.add[10][0],self.add[10][1],self.add[10][2]) #输入企业法人身份证号
        self.wait(2)
        self.upload_file(self.add[11][0],self.add[11][1],self.add[11][2]) #上传企业法人身份证正面
        self.wait(2)
        self.upload_file(self.add[12][0],self.add[12][1],self.add[12][2]) #上传企业法人身份证反面
        self.wait(2)
        self.input_value(self.add[13][0],self.add[13][1],self.add[13][2]) #输入客户联系人姓名
        self.wait(2)
        self.input_value(self.add[14][0],self.add[14][1],self.add[14][2]+self.random_number()) #输入客户联系人电话
        self.wait(2)
        self.input_value(self.add[15][0],self.add[15][1],self.add[15][2]) #输入客户联系人邮箱
        self.wait(2)
        self.input_value(self.add[16][0],self.add[16][1],self.add[16][2]) #输入客户联系人身份证号
        self.wait(2)
        self.upload_file(self.add[17][0],self.add[17][1],self.add[17][2])  #上传客户联系人身份证正面
        self.wait(2)
        self.upload_file(self.add[18][0],self.add[18][1],self.add[18][2])  #上传客户联系人身份证反面
        self.wait(2)
        self.input_value(self.add[19][0],self.add[19][1],self.random_number())  #输入合同编号
        self.wait(2)
        self.input_value(self.add[20][0],self.add[20][1],self.add[20][2])    #输入合同名称
        self.wait(2)
        self.jsp(self.add[21][1]) #输入合同生效日期
        self.wait(2)
        self.jsp(self.add[21][2])
        self.wait(2)
        self.jsp(self.add[22][1]) #输入合同失效日期
        self.wait(2)
        self.jsp(self.add[22][2])
        self.wait(2)
        self.jsp(self.add[24][1]) #输入合同续约日期
        self.wait(2)
        self.jsp(self.add[24][2])
        self.wait(2)
        self.upload_file(self.add[25][0],self.add[25][1],self.add[25][2])  #上传合同附件
        self.wait(2)
        self.click_element(self.add[26][0],self.add[26][1])  #点击确认新建客户按钮
        self.wait(2)
        self.F5()


    def intoformcheck(self,intoway='0'):
        """
        进入客户审核二级菜单内嵌表单页面
        :param way:
        :return:
        """
        self.click_element(self.search[0][0], self.search[0][1])
        self.click_element(self.check[0][0],self.check[0][1])
        self.handleform(0)
        # 判断页面是否存在身份验证
        if intoway=='0':

            if self.isElementExist(findway=self.check[20][0],elementvalue=self.check[20][1]):
                self.wait(40)
                self.click_element(self.check[21][0], self.check[21][1])
                self.wait(5)
            else:
                custmoer_log.csp_log.info('无需身份验证')
        else:
            custmoer_log.csp_log.info(f'进入客户审核二级表单')

    def finding_check(self,check_way=check[1][1],way='0',checkname=add[1][-1],way_number='0'):
        """
        查询已审核或者未审核的客户数据
        :param check_way: 审核的客户类型默认为csp客户
        :param way: 审核类型 已审核或者未审核 默认为未审核
        :param checkname: 审核的客户名称
        :return:
        """
        self.intoformcheck(intoway=way_number)                            #点击进入审核内置表单
        self.click_element(self.check[2][0],check_way)  #点击客户类型
        self.wait(2)
        if way=='0':
            self.click_element(self.check[17][0],self.check[17][1]) #点击待审核
            self.wait(2)
        elif way=='1':
            self.click_element(self.check[18][0],self.check[18][1]) ##点击已审核
            self.wait(2)
        self.input_value(self.check[5][0],self.check[5][1],checkname)  #输入客户名称
        self.click_element(self.check[10][0],self.check[10][1])             #点击查询按钮
        self.wait(2)
    def get_find_check_text(self):
        """
        获取查询的数据客户名称文本值
        :return:
        """
        try:
            value = self.get_text(self.check[11][0],self.check[11][1])
        except Exception:
            custmoer_log.csp_log.exception(f'查询的客户---{self.add[1][-1]}不存在')
            return False
        else:
            custmoer_log.csp_log.info(f'查询的客户----{self.add[1][-1]}存在')
            return value

    def click_check(self,result='0'):
        """
        若查询出待审核数据点击审核按钮开始审核
        :param result:默认审核通过
        :return:
        """
        self.click_element(self.check[12][0],self.check[12][1])  #点击审核按钮
        self.wait(2)

        if result=='1':
            self.click_element(self.check[14][0],self.check[14][1])  #点击审核不通过
            self.wait(2)
            self.input_value(self.check[15][0],self.check[15][1],self.check[15][2])  #输入审核不通过原因
            self.wait(2)
            self.click_element(self.check[16][0], self.check[16][1])  # 点击确认审核按钮
            self.wait(2)
        elif result=='0':
            self.wait(2)

        self.click_element(self.check[16][0], self.check[16][1])  # 点击确认审核按钮
        self.wait(2)
        self.F5()



    def look_check(self):
        """
        查看已审核的数据
        :return:
        """
        self.click_element(self.check[19][0],self.check[19][1])
        self.wait(2)





























