from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *

csp_log = Log(__name__, file=logging.INFO, cmd=logging.INFO)

add_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="add")
search_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="search")
check_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="check")
update_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="update")
other_add = ReadExcel(filepath=test_data + r'\add_csp.xlsx', sheetname='CSP信息申请模板')
grounding_data = ReadExcel(filepath=test_data + r'\test_csp_data.xlsx', sheetname="grounding")


class CspPage(BasePage):
    search = [(search_data.get_excel(1, 3), search_data.get_excel(1, 4)),  # 0点击CSP管理一级菜单
              (search_data.get_excel(2, 3), search_data.get_excel(2, 4)),  # 1点击CSP管理二级菜单
              (search_data.get_excel(3, 3), search_data.get_excel(3, 4)),  # 2输入CSP名称查询
              (search_data.get_excel(4, 3), search_data.get_excel(4, 4)),  # 3输入CSP编码查询
              (search_data.get_excel(5, 3), search_data.get_excel(5, 4), search_data.get_excel(5, 5)),  # 4CSP类型下拉框处理
              (search_data.get_excel(6, 3), search_data.get_excel(6, 4), search_data.get_excel(6, 5)),  # 5CSP状态下拉框处理
              (search_data.get_excel(7, 3), search_data.get_excel(7, 4), search_data.get_excel(7, 5)),  # 6CSP所属省份下拉框处理
              (search_data.get_excel(8, 3), search_data.get_excel(8, 4)),  # 7点击查询按钮
              (search_data.get_excel(9, 3), search_data.get_excel(9, 4)),  # 8点击查看按钮
              (search_data.get_excel(10, 3), search_data.get_excel(10, 4)),  # 9点击上架该csp按钮
              (search_data.get_excel(11, 3), search_data.get_excel(11, 4)),  # 10点击确认上架按钮
              (search_data.get_excel(12,3), search_data.get_excel(12,4),search_data.get_excel(12,5)),  #11点击上传测试报告稿
              (search_data.get_excel(13, 3), search_data.get_excel(13, 4)),  # 12点击提交审核按钮
              ]

    add = [(add_data.get_excel(1, 3), add_data.get_excel(1, 4)),  # 0点击新增CSP按钮
           (add_data.get_excel(2, 3), add_data.get_excel(2, 4), add_data.get_excel(2, 5)),  # 1输入新增的CSP名称
           (add_data.get_excel(3, 3), add_data.get_excel(3, 4), add_data.get_excel(3, 5)),  # 2选择新增的CSP客户类型
           (add_data.get_excel(4, 3), add_data.get_excel(4, 4), add_data.get_excel(4, 5)),  # 3选择csp类型
           (add_data.get_excel(5, 3), add_data.get_excel(5, 4), add_data.get_excel(5, 5)),  # 4选择csp归属省份
           (add_data.get_excel(6, 3), add_data.get_excel(6, 4), add_data.get_excel(6, 5)),  # 5选择csp归属地市
           (add_data.get_excel(7, 3), add_data.get_excel(7, 4), add_data.get_excel(7, 5)),  # 6输入新增的CSP联系人
           (add_data.get_excel(8, 3), add_data.get_excel(8, 4), add_data.get_excel(8, 5)),  # 7输入新增的CSP联系电话
           (add_data.get_excel(9, 3), add_data.get_excel(9, 4), add_data.get_excel(9, 5)),  # 8输入新增的CSP联系人身份证号
           (add_data.get_excel(10, 3), add_data.get_excel(10, 4), add_data.get_excel(10, 5)),  # 9输入新增的CSP联系人邮箱
           (add_data.get_excel(11, 3), add_data.get_excel(11, 4), add_data.get_excel(11, 5)),  # 10上传新增的CSP的经办人身份证正面
           (add_data.get_excel(12, 3), add_data.get_excel(12, 4), add_data.get_excel(12, 5)),  # 11上传新增的CSP的经办人身份证反面
           (add_data.get_excel(13, 3), add_data.get_excel(13, 4), add_data.get_excel(13, 5)),  # 12输入IP地址
           (add_data.get_excel(14, 3), add_data.get_excel(14, 4), add_data.get_excel(14, 5)),  # 13输入CSP回调根目录地址
           (add_data.get_excel(15, 3), add_data.get_excel(15, 4)),  # 14点击系统自动生成token
           (add_data.get_excel(16, 3), add_data.get_excel(16, 4), add_data.get_excel(16, 5)),  # 15输入CSP平台登录地址
           (add_data.get_excel(17, 3), add_data.get_excel(17, 4), add_data.get_excel(17, 5)),  # 16输入CSP平台功能介绍
           (add_data.get_excel(18, 3), add_data.get_excel(18, 4), add_data.get_excel(18, 5)),  # 17上传新增的CSP的平台功能介绍附件
           (add_data.get_excel(19, 3), add_data.get_excel(19, 4)),  # 18输入BIZID
           (add_data.get_excel(20, 3), add_data.get_excel(20, 4)),  # 19输入接入码
           (add_data.get_excel(21, 3), add_data.get_excel(21, 4), add_data.get_excel(21, 5)),  # 20输入法人姓名
           (add_data.get_excel(22, 3), add_data.get_excel(22, 4), add_data.get_excel(22, 5)),  # 21输入法人身份证号
           (add_data.get_excel(23, 3), add_data.get_excel(23, 4), add_data.get_excel(23, 5)),  # 22上传法人身份证正面
           (add_data.get_excel(24, 3), add_data.get_excel(24, 4), add_data.get_excel(24, 5)),  # 23上传法人身份证反面
           (add_data.get_excel(25, 3), add_data.get_excel(25, 4), add_data.get_excel(25, 5)),  # 24输入法人邮箱
           (add_data.get_excel(26, 3), add_data.get_excel(26, 4), add_data.get_excel(26, 5)),  # 25输入注册资金
           (add_data.get_excel(27, 3), add_data.get_excel(27, 4), add_data.get_excel(27, 5)),  # 26处理注册地下拉框
           (add_data.get_excel(28, 3), add_data.get_excel(28, 4), add_data.get_excel(28, 5)),  ##27输入注册地址
           (add_data.get_excel(2,5)+'5'),  #28
           ]

    add_legal = [(add_data.get_excel(29, 3), add_data.get_excel(29, 4), add_data.get_excel(29, 5)),  # 0输入年检度
                 (add_data.get_excel(30, 3), add_data.get_excel(30, 4), add_data.get_excel(30, 5)),  # 1输入经营范围
                 (add_data.get_excel(31, 3), add_data.get_excel(31, 4), add_data.get_excel(31, 5)),  # 2处理是否三证合一下拉框
                 (add_data.get_excel(32, 3), add_data.get_excel(32, 4), add_data.get_excel(32, 5)),  # 3输入统一社会信用代码
                 (add_data.get_excel(33, 3), add_data.get_excel(33, 4), add_data.get_excel(33, 5)),  # 4输入注册号
                 (add_data.get_excel(34, 4), add_data.get_excel(35, 4)),  # 5输入营业开始时间
                 (add_data.get_excel(36, 3), add_data.get_excel(36, 4)),  # 6选择营业结束时间为长期
                 (add_data.get_excel(37, 4), add_data.get_excel(38, 4)),  # 7输入发证时间
                 (add_data.get_excel(39, 3), add_data.get_excel(39, 4), add_data.get_excel(39, 5)),  # 8上传营业执照附件
                 (add_data.get_excel(40, 3), add_data.get_excel(40, 4), add_data.get_excel(40, 5)),  # 9输入税务类型
                 (add_data.get_excel(41, 3), add_data.get_excel(41, 4), add_data.get_excel(41, 5)),  # 10输入税务登记号
                 (add_data.get_excel(42, 3), add_data.get_excel(42, 4), add_data.get_excel(42, 5)),  # 11上传税务登记证附件
                 (add_data.get_excel(43, 3), add_data.get_excel(43, 4), add_data.get_excel(43, 5)),  # 12输入组织机构代码
                 (add_data.get_excel(44, 3), add_data.get_excel(44, 4), add_data.get_excel(44, 5)),  # 13上传组织机构附件
                 (add_data.get_excel(45, 3), add_data.get_excel(45, 4), add_data.get_excel(45, 5)),  # 14输入银行账户类型
                 (add_data.get_excel(46, 3), add_data.get_excel(46, 4), add_data.get_excel(46, 5)),  # 15输入开户名
                 (add_data.get_excel(47, 3), add_data.get_excel(47, 4), add_data.get_excel(47, 5)),  # 16输入开户银行
                 (add_data.get_excel(48, 3), add_data.get_excel(48, 4), add_data.get_excel(48, 5)),  # 17输入银行账号
                 (add_data.get_excel(49, 4), add_data.get_excel(50, 4)),  # 18输入开户时间
                 (add_data.get_excel(51, 3), add_data.get_excel(51, 4), add_data.get_excel(51, 5)),  # 19上传开户许可证附件
                 (add_data.get_excel(52, 3), add_data.get_excel(52, 4), add_data.get_excel(52, 5)),  # 20输入合同编号
                 (add_data.get_excel(53, 3), add_data.get_excel(53, 4), add_data.get_excel(53, 5)),  # 21输入合同名称
                 (add_data.get_excel(54, 4), add_data.get_excel(55, 4)),  # 22输入合同开始时间
                 (add_data.get_excel(56, 4), add_data.get_excel(57, 4)),  # 23输入合同结束时间
                 (add_data.get_excel(58, 3), add_data.get_excel(58, 4), add_data.get_excel(58, 5)),  # 24上传合同附件
                 (add_data.get_excel(59, 3), add_data.get_excel(59, 4)),  # 25点击提交审核按钮
                 (add_data.get_excel(60, 3), add_data.get_excel(60, 4), add_data.get_excel(60, 5)),  # 26点击选择文件
                 (add_data.get_excel(61, 3), add_data.get_excel(61, 4)),  # 27点击开始上传按钮
                 (add_data.get_excel(2,5)+'2'),  #28文件导入新增的csp名称
                 ]

    check = [(check_data.get_excel(1, 3), check_data.get_excel(1, 4)),  # 0点击csp审核二级菜单
             (check_data.get_excel(2, 3), check_data.get_excel(2, 4)),  # 1点击获取验证码
             (check_data.get_excel(3, 3), check_data.get_excel(3, 4)),  # 2点击确认按钮
             (check_data.get_excel(4, 3), check_data.get_excel(4, 4)),  # 3输入csp名称查询
             (check_data.get_excel(5, 3), check_data.get_excel(5, 4)),  # 4输入csp编码查询
             (check_data.get_excel(6, 3), check_data.get_excel(6, 4), check_data.get_excel(6, 5)),  # 5选择CSP类型
             (check_data.get_excel(7, 3), check_data.get_excel(7, 4), check_data.get_excel(7, 5)),  # 6选择CSP状态查询
             (check_data.get_excel(8, 3), check_data.get_excel(8, 4), check_data.get_excel(8, 5)),  # 7选择CSP所属省份
             (check_data.get_excel(9, 3), check_data.get_excel(9, 4), check_data.get_excel(9, 5)),  # 8选择的审核类型
             (check_data.get_excel(10, 3), check_data.get_excel(10, 4)),  # 9点击待审核
             (check_data.get_excel(11, 3), check_data.get_excel(11, 4)),  # 10点击已审核
             (check_data.get_excel(12, 3), check_data.get_excel(12, 4)),  # 11点击查询按钮
             (check_data.get_excel(13, 3), check_data.get_excel(13, 4)),  # 12点击查看待审核的CSP
             (check_data.get_excel(14, 3), check_data.get_excel(14, 4)),  # 13点击审核按钮
             (check_data.get_excel(15, 3), check_data.get_excel(15, 4), check_data.get_excel(15, 5)),  # 14输入审核通过原因
             (check_data.get_excel(16, 3), check_data.get_excel(16, 4)),  # 15点击审核不通过
             (check_data.get_excel(17, 3), check_data.get_excel(17, 4), check_data.get_excel(17, 5)),  # 16输入审核不通过原因
             (check_data.get_excel(18, 3), check_data.get_excel(18, 4)),  # 17审核确定按钮
             (check_data.get_excel(19, 3), check_data.get_excel(19, 4)),  # 18点击查看已审核的CSP
             ]  # 21获取已审核节点csp名称文本值

    update = [(update_data.get_excel(1, 3), update_data.get_excel(1, 4)),  # 0点击编辑按钮
              (update_data.get_excel(2, 3), update_data.get_excel(2, 4), update_data.get_excel(2, 5)),  # 1变更客户类型
              (update_data.get_excel(3, 3), update_data.get_excel(3, 4), update_data.get_excel(3, 5)),  # 2变更csp类型
              (update_data.get_excel(4, 3), update_data.get_excel(4, 4)),  # 3点击提交审核按钮
              (update_data.get_excel(5, 3), update_data.get_excel(5, 4)),  # 4查看页面获取客户类型文本值
              (update_data.get_excel(6, 3), update_data.get_excel(6, 4)),  # 5查看页面获取csp类型文本值
              (update_data.get_excel(7, 3), update_data.get_excel(7, 4)),  # 6点击变更Token手动输入
              (update_data.get_excel(8, 3), update_data.get_excel(8, 4), update_data.get_excel(8, 5)),  # 7手动输入token
              (update_data.get_excel(9, 3), update_data.get_excel(9, 4)),  # 8点击重置密匙
              (update_data.get_excel(10, 3), update_data.get_excel(10, 4)),  # 9点击查看接入密匙变更前后内容
              (update_data.get_excel(11, 3), update_data.get_excel(11, 4)),  # 10点击查看TOKEN变更前后内容
              (update_data.get_excel(12, 3), update_data.get_excel(12, 4)),  # 11点击查看客户类型变更前后内容
              (update_data.get_excel(13, 3), update_data.get_excel(13, 4)),  # 12点击查看csp类型变更前后内容
              (update_data.get_excel(14, 3), update_data.get_excel(14, 4)),  # 13查看页面获取token文本值
              (update_data.get_excel(15, 3), update_data.get_excel(15, 4)),  # 14查看页面获取接入密匙文本值
              ]

    groundingdata = [(grounding_data.get_excel(1, 3), grounding_data.get_excel(1, 4)),  # 0点击上架审核二级菜单
                     (grounding_data.get_excel(2, 3), grounding_data.get_excel(2, 4)),  # 1点击获取上架审核验证码
                     (grounding_data.get_excel(3, 3), grounding_data.get_excel(3, 4)),  # 2点击确认输入验证码按钮
                     (grounding_data.get_excel(4, 3), grounding_data.get_excel(4, 4)),  # 3点击待审核
                     (grounding_data.get_excel(5, 3), grounding_data.get_excel(5, 4)),  # 4输入查询的csp名称
                     (grounding_data.get_excel(6, 3), grounding_data.get_excel(6, 4)),  # 5选择csp类型
                     (grounding_data.get_excel(7, 3), grounding_data.get_excel(7, 4)),  # 6点击查询按钮
                     (grounding_data.get_excel(8, 3), grounding_data.get_excel(8, 4)),  # 7点击审核按钮
                     (grounding_data.get_excel(9, 3), grounding_data.get_excel(9, 4)),  # 8输入审核通过或者不通过原因
                     (grounding_data.get_excel(10, 3), grounding_data.get_excel(10, 4)),  # 9点击确认审核按钮
                     (grounding_data.get_excel(11, 3), grounding_data.get_excel(11, 4)),  # 10点击审核不通过
                     (grounding_data.get_excel(12, 3), grounding_data.get_excel(12, 4)),  # 11点击下架该csp按钮
                     (grounding_data.get_excel(13, 3), grounding_data.get_excel(13, 4)),  # 12点击确定下架按钮
                     (grounding_data.get_excel(14, 3), grounding_data.get_excel(14, 4)),  # 13查看页面点击上架信息编辑按钮
                     (
                     grounding_data.get_excel(15, 3), grounding_data.get_excel(15, 4), grounding_data.get_excel(15, 5)),
                     # 14上传附件
                     (grounding_data.get_excel(16, 3), grounding_data.get_excel(16, 4)),  # 15点击提交审核
                     ]

    other_add_csp = [(other_add.get_excel(2, 1)), ]  # 文件导入的csp名称

    def intoform(self):
        """
        进入csp管理查询内置表单
        :return:
        """

        self.click_element(self.search[0][0], self.search[0][1])
        self.click_element(self.search[1][0], self.search[1][1])
        self.handleform(0)
        self.wait(2)

    def find_csp_data(self, name=add[1][-1],csp_type=add[3][-1]):
        """
        管理csp二级菜单查询出csp数据
        :param name: csp名称
        :param csp_type: csp类型默认为新建的csp类型即“集团csp”
        :return:
        """

        self.intoform()
        self.wait(2)
        self.input_value(self.search[2][0], self.search[2][1], name)  # 输入CSP名称查询
        self.wait(2)
        self.handle_select(self.search[4][0], self.search[4][1],csp_type)  # 选择csp类型
        self.wait(2)
        self.click_element(self.search[7][0], self.search[7][1])  # 点击查询按钮
        self.wait(2)

    def look_csp_data(self):
        """
        查看csp数据
        :return:
        """
        self.click_element(self.search[8][0], self.search[8][1])  # 点击查看按钮
        self.wait(2)


    def update_csp(self, value):
        """
        变更csp客户类型或csp类型
        :param value:1 代表变更csp的客户类型、2 代表变更csp类型 3 代表变更csp的Token值 ，4 代表变更csp的接入密匙
        :return:
        """
        self.click_element(self.update[0][0], self.update[0][1])  # 点击编辑按钮进入编辑页面
        self.wait(2)
        if value == '1':  # 变更客户类型
            self.handle_select(self.update[1][0], self.update[1][1], self.update[1][2])
            self.wait(2)
            self.click_element(self.update[3][0], self.update[3][1])  # 提交变更审核
            self.wait(2)
            self.F5()


        elif value == '2':  # 变更csp类型
            self.handle_select(self.update[2][0], self.update[2][1], self.update[2][2])
            self.wait(2)
            self.click_element(self.update[3][0], self.update[3][1])  # 提交变更审核
            self.wait(2)
            self.F5()


        elif value == '3':  # 变更TOken值
            self.click_element(self.update[6][0], self.update[6][1])  # 点击手动输入
            self.wait(2)
            self.input_value(self.update[7][0], self.update[7][1],self.update[7][2] + self.random_number())  # 输入变更的token值
            self.wait(5)
            self.wait(2)
            self.click_element(self.update[3][0], self.update[3][1])  # 提交变更审核
            self.wait(2)
            self.F5()


        elif value == '4':  # 变更接入密匙
            self.click_element(self.update[8][0], self.update[8][1])
            self.wait(5)
            self.wait(2)
            self.click_element(self.update[3][0], self.update[3][1])  # 提交变更审核
            self.wait(2)
            self.F5()

    def new_csp(self, name=add[1][2]):
        """
        新建 csp
        :return:
        """
        self.intoform()
        self.click_element(self.add[0][0], self.add[0][1])  # 点击新增CSP按钮
        self.wait(2)
        self.input_value(self.add[1][0], self.add[1][1], test_value=name)  # 输入新增的CSP名称
        self.wait(2)
        self.handle_select(self.add[2][0], self.add[2][1], self.add[2][2])  # 选择新增的CSP客户类型
        self.wait(2)
        self.handle_select(self.add[3][0], self.add[3][1], self.add[3][2])  # 选择csp类型
        self.wait(2)
        self.handle_select(self.add[4][0], self.add[4][1], self.add[4][2])  # 选择csp归属省份
        self.wait(2)
        self.handle_select(self.add[5][0], self.add[5][1], self.add[5][2])  # 选择csp归属地市
        self.wait(2)

        self.input_value(self.add[6][0], self.add[6][1], self.add[6][2])  # 输入新增的CSP联系人
        self.wait(2)
        self.input_value(self.add[7][0], self.add[7][1], self.add[7][2])  # 输入新增的CSP联系电话
        self.wait(2)
        self.input_value(self.add[8][0], self.add[8][1], self.add[8][2])  # 输入新增的CSP联系人身份证号
        self.wait(2)
        self.input_value(self.add[9][0], self.add[9][1], self.add[9][2])  # 输入新增的CSP联系人邮箱
        self.wait(2)
        self.upload_file(self.add[10][0], self.add[10][1], self.add[10][2])  # 上传新增的CSP的经办人身份证正面
        self.wait(2)
        self.upload_file(self.add[11][0], self.add[11][1], self.add[11][2])  # 上传新增的CSP的经办人身份证反面
        self.wait(2)
        self.input_value(self.add[12][0], self.add[12][1], self.add[12][2])  # 输入IP地址
        self.wait(2)
        self.input_value(self.add[13][0], self.add[13][1], self.add[13][2])  # 输入CSP回调根目录地址
        self.wait(2)
        self.click_element(self.add[14][0], self.add[14][1])  # 点击系统自动生成token
        self.wait(2)
        self.input_value(self.add[15][0], self.add[15][1], self.add[15][2])  # 输入CSP平台登录地址
        self.wait(2)
        self.input_value(self.add[16][0], self.add[16][1], self.add[16][2])  # 输入CSP平台功能介绍
        self.wait(2)
        self.upload_file(self.add[17][0], self.add[17][1], self.add[17][2])  # 上传新增的CSP的平台功能介绍附件

        self.input_value(self.add[18][0], self.add[18][1], self.random_number())  # 输入BIZID
        self.wait(2)
        self.input_value(self.add[19][0], self.add[19][1], self.random_number())  # 输入接入码
        self.wait(2)
        self.input_value(self.add[20][0], self.add[20][1], self.add[20][2])  # 输入法人姓名
        self.wait(2)
        self.input_value(self.add[21][0], self.add[21][1], self.add[21][2])  # 输入法人身份证号
        self.wait(2)
        self.upload_file(self.add[22][0], self.add[22][1], self.add[22][2])  # 上传法人身份证正面
        self.wait(2)
        self.upload_file(self.add[23][0], self.add[23][1], self.add[23][2])  # 上传法人身份证反面
        self.wait(2)
        self.input_value(self.add[24][0], self.add[24][1], self.add[24][2])  # 输入法人邮箱
        self.wait(2)
        self.input_value(self.add[25][0], self.add[25][1], self.random_number())  # 输入注册资金
        self.wait(2)
        self.input_value(self.add[26][0], self.add[26][1], self.add[26][2])  # 处理注册地下拉框
        self.wait(2)
        self.input_value(self.add[27][0], self.add[27][1], self.add[27][2])  # 输入注册地址
        self.wait(2)

        self.input_value(self.add_legal[0][0], self.add_legal[0][1], self.add_legal[0][2])  # 输入年检度
        self.wait(2)
        self.input_value(self.add_legal[1][0], self.add_legal[1][1], self.add_legal[1][2])  # 输入经营范围
        self.wait(2)
        self.handle_select(self.add_legal[2][0], self.add_legal[2][1], self.add_legal[2][2])  # 处理是否三证合一下拉框
        self.wait(2)
        self.input_value(self.add_legal[3][0], self.add_legal[3][1],
                         self.random_number() + self.random_number())  # 输入统一社会信用代码
        self.wait(2)
        self.input_value(self.add_legal[4][0], self.add_legal[4][1],
                         self.random_number() + self.random_number())  # 输入注册号
        self.wait(2)
        self.jsp(self.add_legal[5][0])
        self.wait(2)
        self.jsp(self.add_legal[5][1])  # 输入营业开始时间
        self.wait(2)
        self.click_element(self.add_legal[6][0], self.add_legal[6][1])  # 选择营业结束时间为长期
        self.wait(2)
        self.jsp(self.add_legal[7][0])
        self.wait(2)
        self.jsp(self.add_legal[7][1])  # 输入发证时间
        self.wait(2)
        self.upload_file(self.add_legal[8][0], self.add_legal[8][1], self.add_legal[8][2])  # 上传营业执照附件
        self.wait(2)
        self.input_value(self.add_legal[9][0], self.add_legal[9][1], self.add_legal[9][2])  # 输入税务类型
        self.wait(2)
        self.input_value(self.add_legal[10][0], self.add_legal[10][1],
                         self.random_number() + self.random_number())  # 输入税务登记号
        self.wait(2)
        self.upload_file(self.add_legal[11][0], self.add_legal[11][1], self.add_legal[11][2])  # 上传税务登记证附件
        self.wait(2)
        self.input_value(self.add_legal[12][0], self.add_legal[12][1], self.random_number())  # 输入组织机构代码
        self.wait(2)
        self.upload_file(self.add_legal[13][0], self.add_legal[13][1], self.add_legal[13][2])  # 上传组织机构附件
        self.wait(2)
        self.input_value(self.add_legal[14][0], self.add_legal[14][1], self.add_legal[14][2])  # 输入银行账户类型
        self.wait(2)
        self.input_value(self.add_legal[15][0], self.add_legal[15][1], self.add_legal[15][2])  # 输入开户名
        self.wait(2)
        self.input_value(self.add_legal[16][0], self.add_legal[16][1], self.add_legal[16][2])  # 输入开户银行
        self.wait(2)
        self.input_value(self.add_legal[17][0], self.add_legal[17][1],
                         self.add_legal[17][2] + self.random_number())  # 输入银行账号
        self.wait(2)
        self.jsp(self.add_legal[18][0])
        self.wait(2)
        self.jsp(self.add_legal[18][1])  # 输入开户时间
        self.wait(2)
        self.upload_file(self.add_legal[19][0], self.add_legal[19][1], self.add_legal[19][2])  # 上传开户许可证附件
        self.wait(2)
        self.input_value(self.add_legal[20][0], self.add_legal[20][1], self.random_number())  # 输入合同编号
        self.wait(2)
        self.input_value(self.add_legal[21][0], self.add_legal[21][1], self.add_legal[21][2])  # 输入合同名称
        self.wait(2)
        self.jsp(self.add_legal[22][0])
        self.wait(2)
        self.jsp(self.add_legal[22][1])  # 输入合同开始时间
        self.wait(2)
        self.jsp(self.add_legal[23][0])
        self.wait(2)
        self.jsp(self.add_legal[23][1])  # 输入合同结束时间
        self.wait(2)
        self.upload_file(self.add_legal[24][0], self.add_legal[24][1], self.add_legal[24][2])  # 上传合同附件
        self.wait(2)
        self.click_element(self.add_legal[25][0], self.add_legal[25][1])  # 点击提交审核
        self.wait(2)
        self.F5()

    def intocheck(self, way='0'):
        """
        进入审核csp内置表单
        :param way:
        :return:
        """
        self.click_element(self.search[0][0], self.search[0][1])
        self.wait(2)
        self.click_element(self.check[0][0], self.check[0][1])
        self.handleform(0)

        # 判断页面是否存在身份验证
        if way == '0':

            if self.isElementExist(self.check[1][0], self.check[1][1]):
                self.wait(40)
                self.click_element(self.check[2][0], self.check[2][1])
                self.wait(2)
            else:
                csp_log.csp_log.info('无需身份验证')
        else:
            csp_log.csp_log.info(f'进入chatbot审核二级表单')

    def find_check_csp(self, cspname=add[1][-1], check_type='0',check_csp_type=add[3][-1]):
        """
        csp审核二级菜单查询待审核或已审核的csp
        :param cspname:
        :param check_type:
        :return:
        """
        if check_type == '0':
            self.click_element(self.check[9][0], self.check[9][1])  # 点击待审核
            self.wait(2)
        else:
            self.click_element(self.check[10][0], self.check[10][1])  # 点击已审核
            self.wait(2)

        self.input_value(self.check[3][0], self.check[3][1], cspname)  # 输入查询条件
        self.wait(2)
        self.handle_select(self.check[5][0], self.check[5][1],check_csp_type)  # 选择csp类型
        self.click_element(self.check[11][0], self.check[11][1])  # 点击查询
        self.wait(2)

    def look_check_csp(self):
        """
        查看待审核的数据
        :return:
        """
        self.click_element(self.check[12][0], self.check[12][1])  # 点击查看按钮
        self.wait(2)

    def look_checked_csp(self):
        """
        点击查看已经审核的csp数据
        :return:
        """
        self.click_element(self.check[18][0], self.check[18][1])
        self.wait(2)

    def starting_check(self, result='0'):
        """
        开始审核
        :param result:
        :return:
        """
        self.click_element(self.check[13][0], self.check[13][1])  # 点击审核按钮
        self.wait(2)
        if result == '0':  # 审核通过
            self.input_value(self.check[14][0], self.check[14][1], self.check[14][2])  # 输入审核通过原因
            self.wait(2)

        else:
            self.click_element(self.check[15][0], self.check[15][1])  # 点击审核不通过
            self.wait(2)
            self.input_value(self.check[16][0], self.check[16][1], self.check[16][2])  # 输入审核不通过原因

        self.wait(2)
        self.click_element(self.check[17][0], self.check[17][1])  # 点击确认审核结果
        self.wait(2)
        self.F5()

    def look_update(self, text):
        """
        查看变更的内容
        :param text:
        :return:
        """

        if text == '1':  # 查看token变更内容

            token_value = self.isElementExist(self.update[10][0], self.update[10][1])
            self.wait(2)
            return token_value

        elif text == '2':  # 查看接入密匙前后变更内容

            code_value = self.isElementExist(self.update[9][0], self.update[9][1])
            self.wait(2)
            return code_value

        elif text == '3':  # 点击查看客户类型变更前后内容
            self.isElementExist(self.update[11][0], self.update[11][1])
            self.wait(2)

        elif text == '4':  # 点击查看csp类型变更前后内容

            self.isElementExist(self.update[12][0], self.update[12][1])
            self.wait(2)

    def grounding_on(self):
        """
        csp管理二级菜单查询出数据点击查看进入页面进行上架操作
        :return:
        """
        self.click_element(self.search[9][0], self.search[9][1])  # 点击上架该csp
        self.wait(2)
        self.click_element(self.search[10][0], self.search[10][1])  # 点击确认上架
        self.wait(2)
        self.upload_file(self.search[11][0], self.search[11][1], self.search[11][2])  # 上传报告
        self.wait(2)
        self.click_element(self.search[12][0], self.search[12][1])  # 点击确认提交审核按钮
        self.wait(2)
        self.F5()

    def grounding_off(self):
        """
        csp管理二级菜单查询出数据点击查看进入页面操作下架
        :return:
        """
        self.click_element(self.groundingdata[11][0], self.groundingdata[11][1])  # 点击下架按钮
        csp_log.csp_log.info('进入csp查看页面点击下架按钮')
        self.wait(2)
        self.click_element(self.groundingdata[12][0], self.groundingdata[12][1])  # 点击确定下架按钮
        csp_log.csp_log.info('点击确定下架按钮')
        self.wait(2)
        self.F5()

    def grounding_on_again(self):
        """
        csp管理二级菜单查询存在过上架记录且当前csp状态为已下架的csp数据，查看页面操作再次上架申请
        :return:
        """
        self.click_element(self.groundingdata[13][0], self.groundingdata[13][1])  # 查看页面点击上架申请记录的编辑按钮
        csp_log.csp_log.info('点击编辑按钮')
        self.wait(2)
        self.upload_file(self.groundingdata[14][0], self.groundingdata[14][1], self.groundingdata[14][2])  # 上传附件
        csp_log.csp_log.info('点击csp上架上传文件按钮')
        self.wait(2)
        self.click_element(self.groundingdata[15][0], self.groundingdata[15][1])  # 点击提交审核
        csp_log.csp_log.info('点击提交审核按钮')
        self.wait(2)
        self.F5()

    def grouding_check_form(self, grounding_way='0'):
        """
        进入上架审核二级菜单
        :param grounding_way:
        :return:
        """
        self.click_element(self.search[0][0], self.search[0][1])
        self.click_element(self.groundingdata[0][0], self.groundingdata[0][1])
        self.handleform(0)

        if grounding_way == '0':

            if self.isElementExist(self.groundingdata[1][0], self.groundingdata[1][1]):
                self.wait(40)
                self.click_element(self.groundingdata[2][0], self.groundingdata[2][1])
                self.wait(2)
            else:
                csp_log.csp_log.info('无需身份验证')
        else:
            csp_log.csp_log.info(f'进入chatbot审核二级表单')

    def find_grounding_data(self, grounding_name=add[1][-1],gronding_csp_type=add[3][-1]):
        """
        查询出待审核的上架申请数据
        :param grounding_name:
        :return:
        """
        self.click_element(self.groundingdata[3][0], self.groundingdata[3][1])  # 点击待审核
        csp_log.csp_log.info('点击待审核按钮')
        self.wait(2)
        self.input_value(self.groundingdata[4][0], self.groundingdata[4][1],grounding_name)  # 输入查询条件
        csp_log.csp_log.info(f'输入客户名称{grounding_name}')
        self.wait(2)
        self.handle_select(self.groundingdata[5][0], self.groundingdata[5][1],gronding_csp_type)  # 选择csp类型
        self.wait(2)
        csp_log.csp_log.info(f'选择csp类型{gronding_csp_type}')
        self.click_element(self.groundingdata[6][0], self.groundingdata[6][1])  # 点击查询按钮
        csp_log.csp_log.info(f'点击查看按钮')
        self.wait(2)

    def check_grounding(self, result='1'):
        """
        审核页面，开始审核上架申请
        :param result:
        :return:
        """
        self.wait(5)
        self.click_element(self.groundingdata[7][0], self.groundingdata[7][1])  # 点击审核按钮
        csp_log.csp_log.info('点击审核按钮')
        if result == '1':
            # 审核通过
            self.input_value(self.groundingdata[8][0], self.groundingdata[8][1], self.random_number())
            csp_log.csp_log.info(f'选择审核通过，输入审核通过原因')
            self.wait(2)

        elif result == '0':
            # 审核不同过
            self.click_element(self.groundingdata[10][0], self.groundingdata[10][1])  # 点击审核不通过
            csp_log.csp_log.info('点击审核不通过按钮')
            self.wait(2)
            self.input_value(self.groundingdata[8][0], self.groundingdata[8][1], self.random_number())
            csp_log.csp_log.info(f'选择审核不通过，输入审核不通过原因')
            self.wait(2)

        self.click_element(self.groundingdata[9][0], self.groundingdata[9][1])  # 点击确认审核
        self.wait(2)
        self.F5()

    def look_gronding(self, result=search[5][-1]):
        """
        查询已经上架或者下架的csp
        :param result:
        :param more: 查询出数据后更多的操作默认不点击查看
        :return:
        """

        self.intoform()  # 进入csp管理内置表单
        self.wait(2)
        self.handle_select(self.search[5][0], self.search[5][1],result)  # 选择csp状态
        csp_log.csp_log.info(f'csp上架审核节点选择csp状态---{result}')
        self.wait(2)
        self.input_value(self.search[2][0], self.search[2][1], self.add[1][-1])  # 输入csp名称
        csp_log.csp_log.info(f'csp上架审核节点输入csp名称---{self.add[1][-1]}')
        self.click_element(self.search[7][0],self.search[7][1])
        csp_log.csp_log.info('点击查询按钮')
        self.wait(2)

    def get_assert_text(self, text=add[1][-1]):
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


    def other_add(self):
        """

        :return:
        """
        self.intoform()
        self.click_element(self.add[0][0], self.add[0][1])  # 点击新增CSP按钮
        self.wait(2)
        self.upload_file(self.add_legal[26][0], self.add_legal[26][1], self.add_legal[26][2])  # 上传文件
        self.wait(2)
        self.click_element(self.add_legal[27][0], self.add_legal[27][1])  # 点击开始上传
        self.wait(2)
        self.input_value(self.add[1][0], self.add[1][1],self.add_legal[28])  # 输入csp名称
        self.wait(2)
        self.upload_file(self.add[10][0], self.add[10][1], self.add[10][2])  # 上传新增的CSP的经办人身份证正面
        self.wait(2)
        self.upload_file(self.add[11][0], self.add[11][1], self.add[11][2])  # 上传新增的CSP的经办人身份证反面
        self.wait(2)
        self.click_element(self.add[14][0], self.add[14][1])  # 点击系统自动生成token
        self.wait(2)
        self.upload_file(self.add[17][0], self.add[17][1], self.add[17][2])  # 上传新增的CSP的平台功能介绍附件
        self.wait(2)
        self.input_value(self.add[19][0], self.add[19][1], self.random_number())  # 输入接入码
        self.wait(2)
        self.upload_file(self.add[22][0], self.add[22][1], self.add[22][2])  # 上传法人身份证正面
        self.wait(2)
        self.upload_file(self.add[23][0], self.add[23][1], self.add[23][2])  # 上传法人身份证反面
        self.wait(2)
        self.upload_file(self.add_legal[8][0], self.add_legal[8][1], self.add_legal[8][2])  # 上传营业执照附件
        self.wait(2)
        self.upload_file(self.add_legal[11][0], self.add_legal[11][1], self.add_legal[11][2])  # 上传税务登记证附件
        self.wait(2)
        self.upload_file(self.add_legal[13][0], self.add_legal[13][1], self.add_legal[13][2])  # 上传组织机构附件
        self.wait(2)
        self.upload_file(self.add_legal[19][0], self.add_legal[19][1], self.add_legal[19][2])  # 上传开户许可证附件
        self.wait(2)
        self.upload_file(self.add_legal[24][0], self.add_legal[24][1], self.add_legal[24][2])  # 上传合同附件
        self.wait(2)
        self.click_element(self.add_legal[25][0], self.add_legal[25][1])  # 点击提交审核
        self.wait(2)
        self.F5()


if __name__ == '__main__':
    pass


