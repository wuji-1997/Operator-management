from common.my_log import Log
import logging
from Page.base_page import BasePage
from common.readexcel import ReadExcel
from config.Conf import *

chatbot_log=Log(__name__,file=logging.INFO,cmd=logging.INFO)
search_data=ReadExcel(filepath=test_data+r'\test_chatbot_data.xlsx',sheetname="search")
add_data  =ReadExcel(filepath=test_data+r'\test_chatbot_data.xlsx',sheetname="add")
update_data  =ReadExcel(filepath=test_data+r'\test_chatbot_data.xlsx',sheetname="update")
check_data  =ReadExcel(filepath=test_data+r'\test_chatbot_data.xlsx',sheetname="check")


class  ChatbotPage(BasePage):

    adddate=[(add_data.get_excel(1,3),add_data.get_excel(1,4)),  #0点击新增Chatbot按钮
             (add_data.get_excel(2,3),add_data.get_excel(2,4)),  #1点击归属CSP按钮
             (add_data.get_excel(3,3),add_data.get_excel(3,4),add_data.get_excel(3,5)),  #2输入CSP名称
             (add_data.get_excel(4,3),add_data.get_excel(4,4)),  #3点击CSP查询按钮
             (add_data.get_excel(5,3),add_data.get_excel(5,4)), #4点击选择CSP
             (add_data.get_excel(6,3),add_data.get_excel(6,4)),  #5点击确认选择
             (add_data.get_excel(7,3),add_data.get_excel(7,4)),  #6点击选择客户
             (add_data.get_excel(8,3),add_data.get_excel(8,4),add_data.get_excel(8,5)),    #7输入企业客户名称
             (add_data.get_excel(9,3),add_data.get_excel(9,4)),  #8点击查询按钮
             (add_data.get_excel(10,3),add_data.get_excel(10,4),add_data.get_excel(10,5)),  #9
             (add_data.get_excel(11,3),add_data.get_excel(11,4)),  #10
             (add_data.get_excel(12,3),add_data.get_excel(12,4)),  #11点击选择某一个客户
             (add_data.get_excel(13,3),add_data.get_excel(13,4)),   #12点击确认按钮
             (add_data.get_excel(14,3),add_data.get_excel(14,4),add_data.get_excel(14,5)),   #13输入新建的Chatbot名称
             (add_data.get_excel(15,3),add_data.get_excel(15,4)),  #14输入Chatbot ID
             (add_data.get_excel(16,3),add_data.get_excel(16,4),add_data.get_excel(16,5)),   #15点击上传chatbot头像按钮
             (add_data.get_excel(17,3),add_data.get_excel(17,4),add_data.get_excel(17,5)),  #16输入服务信息
             (add_data.get_excel(18,3),add_data.get_excel(18,4),add_data.get_excel(18,5)),  #17输入签名
             (add_data.get_excel(19,3),add_data.get_excel(19,4),add_data.get_excel(19,5)), #18选择行业类型
             (add_data.get_excel(20,3),add_data.get_excel(20,4)),  #19选择是否显示Chatbot提供者
             (add_data.get_excel(21,3),add_data.get_excel(21,4),add_data.get_excel(21,5)),   #20输入服务条款
             (add_data.get_excel(22,3),add_data.get_excel(22,4),add_data.get_excel(22,5)),  #21输入Chatbot邮箱
             (add_data.get_excel(23,3),add_data.get_excel(23,4),add_data.get_excel(23,5)),  #22输入Chatbot官网
             (add_data.get_excel(24,3),add_data.get_excel(24,4),add_data.get_excel(24,5)),  #23输入Chatbot服务电话
             (add_data.get_excel(25,3),add_data.get_excel(25,4),add_data.get_excel(25,5)),  #24选择省份
             (add_data.get_excel(26,3),add_data.get_excel(26,4),add_data.get_excel(26,5)),  #25选择地市
             (add_data.get_excel(27,3),add_data.get_excel(27,4),add_data.get_excel(27,5)),  #26选择县区
             (add_data.get_excel(28,3),add_data.get_excel(28,4),add_data.get_excel(28,5)),  #27输入具体地址
             (add_data.get_excel(29,3),add_data.get_excel(29,4),add_data.get_excel(29,5)),  #28输入纬度
             (add_data.get_excel(30,3),add_data.get_excel(30,4),add_data.get_excel(30,5)),  #29输入经度
             (add_data.get_excel(31,3),add_data.get_excel(31,4),add_data.get_excel(31,5)),  #30输入ip地址
             (add_data.get_excel(32,3),add_data.get_excel(32,4)),   #31点击新增IP地址
             (add_data.get_excel(33,3),add_data.get_excel(33,4),add_data.get_excel(33,5)),  #32输入新增的ip地址
             (add_data.get_excel(34,3),add_data.get_excel(34,4)),  #33点击提交新增的CHatbot
             add_data.get_excel(14,5)+"1",   #34
             ]

    searchdata=[(search_data.get_excel(1,3),search_data.get_excel(1,4)),   #0点击Chatbot管理一级菜单
                (search_data.get_excel(2,3),search_data.get_excel(2,4)),   #1点击Chatbot管理二级菜单
                (search_data.get_excel(3,3),search_data.get_excel(3,4)),   #2点击Chatbot固定菜单审核二级菜单
                (search_data.get_excel(4,3),search_data.get_excel(4,4)),   #3点击选择cahtbot管理
                (search_data.get_excel(5,3),search_data.get_excel(5,4)),  #4输入Chatbot名称查询
                (search_data.get_excel(6,3),search_data.get_excel(6,4),search_data.get_excel(6,5)),  #5输入ChatbotID查询
                (search_data.get_excel(7,3),search_data.get_excel(7,4),search_data.get_excel(7,5)),  #6输入企业客户名称查询
                (search_data.get_excel(8,3),search_data.get_excel(8,4),search_data.get_excel(8,5)),  #7输入企业客户id查询
                (search_data.get_excel(9,3),search_data.get_excel(9,4),search_data.get_excel(9,5)),  #8选择接入类型查询
                (search_data.get_excel(10,3),search_data.get_excel(10,4),search_data.get_excel(10,5)),  #9选择CSP状态查询
                (search_data.get_excel(11,3),search_data.get_excel(11,4)),  #10点击查询按钮
                (search_data.get_excel(12,3),search_data.get_excel(12,4)),  #11查询出数据点击查看按钮
                (search_data.get_excel(13,3),search_data.get_excel(13,4)),  #12获取查询出的chatbot文本值
                (search_data.get_excel(14,3),search_data.get_excel(14,4)),  #13获取查看页面chatbotid文本值
                ]

    checkdata=[(check_data.get_excel(1,3),check_data.get_excel(1,4)),    #0点击Chatbot审核二级菜单
               (check_data.get_excel(2,3),check_data.get_excel(2,4)),    #1点击待审核按钮
               (check_data.get_excel(3,3),check_data.get_excel(3,4)),    #2点击已审核按钮
               (check_data.get_excel(4,3),check_data.get_excel(4,4)),    #3待审核节点输入Chatbot名称
               (check_data.get_excel(5,3),check_data.get_excel(5,4),check_data.get_excel(5,5)), #4选择chatbot接入类型
               (check_data.get_excel(6,3),check_data.get_excel(6,4)),   #5点击查询按钮
               (check_data.get_excel(7,3),check_data.get_excel(7,4)),   #6获取待审核节点查询出的chatbot名称文本
               (check_data.get_excel(8,3),check_data.get_excel(8,4)),  #7点击审核按钮
               (check_data.get_excel(9,3),check_data.get_excel(9,4)), #8点击审核不通过
               (check_data.get_excel(10,3),check_data.get_excel(10,4),check_data.get_excel(10,5)),  #9输入审核不通过原因
               (check_data.get_excel(11,3),check_data.get_excel(11,4)),   #10点击确定审核按钮
               (check_data.get_excel(12,3),check_data.get_excel(12,4)),   #11获取已审核节点查询出的chatbot名称文本
               (check_data.get_excel(13,3),check_data.get_excel(13,4)),   #12查询出已审核的chatbot数据点击查看按钮
               (check_data.get_excel(14,3),check_data.get_excel(14,4)),   #13获取查看页面chatbotid文本值
               (check_data.get_excel(15,3),check_data.get_excel(15,4)),   #14点击获取验证码
               (check_data.get_excel(16,3),check_data.get_excel(16,4)),   #15确认输入的验证码
               ]

    updatedata=[(update_data.get_excel(1,3),update_data.get_excel(1,4)),  #0chatbot查看页面点击chatbot详情编辑按钮
                (update_data.get_excel(2,3),update_data.get_excel(2,4),update_data.get_excel(2,5)),  #1变更chatbot名称
                (update_data.get_excel(3,3),update_data.get_excel(3,4)),  #2点击提交审核按钮
                (update_data.get_excel(4,3),update_data.get_excel(4,4),update_data.get_excel(4,5)),  #3点击chatbot配置编辑按钮
                (update_data.get_excel(5,3),update_data.get_excel(5,4),update_data.get_excel(5,5)),  #4变更Chatbot速率
                (update_data.get_excel(6,3),update_data.get_excel(6,4),update_data.get_excel(6,5)),  #5点击确定按钮
                (update_data.get_excel(7,3),update_data.get_excel(7,4),update_data.get_excel(7,5)),  #6点击注销chatbot
                (update_data.get_excel(8,3),update_data.get_excel(8,4),update_data.get_excel(8,5)),  #7点击确认注销chatbot
                'update',  #8
                (update_data.get_excel(9,3),update_data.get_excel(9,4)),   #9更新审核结果确定按钮
                (update_data.get_excel(10,3),update_data.get_excel(10,4)), #10更新选择审核不通过
                (update_data.get_excel(11,3),update_data.get_excel(11,4),update_data.get_excel(11,5)),  #11更新输入审核不通过原因
                ]
    new_chatbot = adddate[13][-1] + updatedata[8]



    def intoform(self):
        """
        进入csp管理二级菜单内置表单
        :return:
        """
        self.click_element(self.searchdata[0][0],self.searchdata[0][1])
        self.click_element(self.searchdata[1][0],self.searchdata[1][1])
        self.handleform(0)

    def add_chatbot(self,name=adddate[13][-1]):
        """
        新增一个chatbot
        :param name:
        :return:
        """
        self.intoform()  #进入内置表单
        self.wait(2)
        self.click_element(self.adddate[0][0],self.adddate[0][1])  #点击新增chatbot按钮
        self.wait(2)
        self.click_element(self.adddate[1][0],self.adddate[1][1])  #点击归属CSP按钮
        self.wait(2)
        self.input_value(self.adddate[2][0],self.adddate[2][1],self.adddate[2][2])    #输入csp名称
        self.wait(2)
        self.click_element(self.adddate[3][0],self.adddate[3][1])  #点击查询按钮
        self.wait(2)
        self.click_element(self.adddate[4][0],self.adddate[4][1])  #点击选择csp
        self.wait(2)
        self.click_element(self.adddate[5][0],self.adddate[5][1])  #点击确认选择
        self.wait(2)
        self.click_element(self.adddate[6][0],self.adddate[6][1])  #点击选择客户
        self.wait(2)
        self.input_value(self.adddate[7][0],self.adddate[7][1],self.adddate[7][2])  #输入企业客户名称
        self.wait(2)
        self.click_element(self.adddate[8][0],self.adddate[8][1])  #点击查询按钮
        self.wait(2)
        self.click_element(self.adddate[11][0],self.adddate[11][1])  #点击选择某一个客户
        self.wait(2)
        self.click_element(self.adddate[12][0],self.adddate[12][1])  #点击确认选择
        self.wait(2)
        self.input_value(self.adddate[13][0],self.adddate[13][1],name)  #输入新建的chatbot名称
        self.wait(2)
        self.input_value(self.adddate[14][0],self.adddate[14][1],self.random_number())  #输入cahtbotid
        self.wait(2)
        self.upload_file(self.adddate[15][0],self.adddate[15][1],self.adddate[15][2])  #上传chatbot头像
        self.wait(2)
        self.input_value(self.adddate[16][0],self.adddate[16][1],self.adddate[16][2]+self.random_number())  #输入服务信息
        self.wait(2)
        self.input_value(self.adddate[17][0],self.adddate[17][1],self.adddate[17][2]+self.random_number())  #输入签名
        self.wait(2)
        self.handle_select(self.adddate[18][0],self.adddate[18][1],self.adddate[18][2])  #选择行业类型
        self.wait(2)
        self.input_value(self.adddate[20][0],self.adddate[20][1],self.adddate[20][2]+self.random_number()) #输入服务条款
        self.wait(2)
        self.input_value(self.adddate[21][0],self.adddate[21][1],self.adddate[21][2])  #输入Chatbot邮箱
        self.wait(2)
        self.input_value(self.adddate[22][0],self.adddate[22][1],self.adddate[22][2])  #输入Chatbot官网
        self.wait(2)
        self.input_value(self.adddate[23][0],self.adddate[23][1],self.adddate[23][2])  #输入Chatbot服务电话
        self.wait(2)
        self.handle_select(self.adddate[24][0], self.adddate[24][1], self.adddate[24][2]) #选择省份
        self.wait(2)
        self.handle_select(self.adddate[25][0], self.adddate[25][1], self.adddate[25][2]) #选择地市
        self.wait(2)
        self.handle_select(self.adddate[26][0], self.adddate[26][1], self.adddate[26][2]) #选择县区
        self.wait(2)
        self.input_value(self.adddate[27][0], self.adddate[27][1], self.adddate[27][2])   #输入具体地址
        self.wait(2)
        self.input_value(self.adddate[28][0], self.adddate[28][1], self.adddate[28][2])   #输入纬度
        self.wait(2)
        self.input_value(self.adddate[29][0], self.adddate[29][1], self.adddate[29][2])   #输入经度
        self.wait(2)
        self.input_value(self.adddate[30][0], self.adddate[30][1], self.adddate[30][2])   #输入ip地址
        self.wait(2)
        #self.click_element(self.adddate[31][0],self.adddate[31][1])   #点击新增ip地址
        #self.wait(2)
        #self.input_value(self.adddate[32][0],self.adddate[32][1],self.adddate[32][2]) #输入新增的ip地址
        #self.wait(2)
        self.click_element(self.adddate[33][0],self.adddate[33][1])  #点击确认新增
        self.wait(2)
        self.F5()


    def find_chatbot(self,chatbotname=adddate[13][-1]):
        """
        csp管理二级菜单输入chatbot名称和选择chatbot接入类型查询数据
        :param chatbotname:
        :return:
        """
        self.intoform()  #进入管理节点内置表单
        self.input_value(self.searchdata[4][0],self.searchdata[4][1],chatbotname)  #输入chatbot名称
        self.handle_select(self.searchdata[8][0],self.searchdata[8][1],self.searchdata[8][2]) #选择chatbot接入类型
        self.wait(2)
        self.click_element(self.searchdata[10][0],self.searchdata[10][1])  #点击查询按钮
        self.wait(2)

    def get_cahtbot_text(self):
        """
        获取查询出的cahtbot名称文本值
        :return:
        """
        try:
            value = self.get_text(self.searchdata[12][0],self.searchdata[12][1])    #获取客户名称文本值
        except Exception:
            chatbot_log.csp_log.exception(f'查询的客户不存在')
            return False
        else:
            chatbot_log.csp_log.info(f'查询到客户{self.adddate[13][-1]}')
            return value

    def into_lookover(self,code='0'):
        """
        进入chatbot查看页面且返回chatbotid文本值
        :param code:
        :return:
        """
        self.click_element(self.searchdata[11][0],self.searchdata[11][1])  #点击查看按钮
        self.wait(2)
        value =self.get_text(self.searchdata[13][0],self.searchdata[13][1])
        if code=='0':
            chatbot_log.csp_log.info('获取chatbotid文本值成功')
            return value
        else:
            chatbot_log.csp_log.info('未获取chatbotid的文本值')


    def update_chatbot(self,update_msg='0'):
        """
        变更chatbot信息
        :param update_msg:
        :return:
        """
        if update_msg=='0':

            self.click_element(self.updatedata[0][0],self.updatedata[0][1])   #点击chatbot信息编辑按钮
            self.wait(2)
            self.clear_input(self.updatedata[1][0],self.updatedata[1][1])     #清空chatbot名称输入框
            self.input_value(self.updatedata[1][0],self.updatedata[1][1],self.new_chatbot)  #输入新的chatbot名称
            self.click_element(self.updatedata[2][0],self.updatedata[2][1])  #点击确认变更按钮
            self.wait(2)
            self.F5()
        else:
            self.click_element(self.updatedata[3][0],self.updatedata[3][1])   #点击chatbot配置编辑按钮
            self.wait(2)
            self.clear_input(self.updatedata[4][0],self.updatedata[4][1])    #清空chatbot信息发送速率输入框
            self.input_value(self.updatedata[4][0],self.updatedata[4][1],self.updatedata[4][2]) #输入变更的chatbot速率
            self.click_element(self.updatedata[5][0],self.updatedata[5][1])  #点击确认变更按钮
            self.wait(2)
            self.F5()

    def delete_chatbot(self):
        """
        注销chatbot
        :return:
        """
        self.click_element(self.updatedata[6][0],self.updatedata[6][1])   #点击注销chatbot按钮
        self.wait(2)
        self.click_element(self.updatedata[7][0],self.updatedata[7][1])   #点击确认注销
        self.wait(2)
        self.F5()

    def intocheck(self,way='0'):
        """
        进入chatbot审核内置表单
        :param way:默认需要身份验证
        :return:
        """
        self.click_element(self.searchdata[0][0],self.searchdata[0][1])
        self.click_element(self.checkdata[0][0],self.checkdata[0][1])
        self.handleform(0)
        # 判断页面是否存在身份验证
        if way == '0':

            if self.isElementExist(self.checkdata[14][0],self.checkdata[14][1]):
                self.wait(40)
                self.click_element(self.checkdata[15][0],self.checkdata[15][1])
                self.wait(5)
            else:
                chatbot_log.csp_log.info('无需身份验证')
        else:
            chatbot_log.csp_log.info(f'进入chatbot审核二级表单')


    def find_check(self,status='0',check_chatbotname=adddate[13][-1]):
        """
        查询出已审核或者待审核的数据
        :param status: chatbot审核状态默认0为待审核
        :param check_chatbotname: 查询待审核或已审核的chatbot名称
        :return:
        """
        if status=='0':
           self.click_element(self.checkdata[1][0],self.checkdata[1][1])  #点击待审核
           self.wait(2)
        elif status=='1':
            self.click_element(self.checkdata[2][0],self.checkdata[2][1])  #点击已审核按钮
            self.wait(2)

        self.input_value(self.checkdata[3][0], self.checkdata[3][1],check_chatbotname)  # 输入待审核的chatbot名称
        self.handle_select(self.checkdata[4][0], self.checkdata[4][1], self.checkdata[4][2])  # 选择接入类型
        self.wait(2)
        self.click_element(self.checkdata[5][0], self.checkdata[5][1])  # 点击查询按钮



    def assert_chatbotname(self,chatbot_name=adddate[13][-1]):
        """
        判断某个节点chatbot名称是否存在
        :param chatbot_name:
        :return:
        """

        value = f'<td>{chatbot_name}</td>'
        return value

    def look_checked_chatbot(self):
        """
        查看已经审核的chatbot
        :return:
        """
        self.find_check(status='1') #查询出已经审核的chatbot数据
        self.click_element(self.checkdata[12][0],self.checkdata[12][1]) #点击查看按钮
        vlaue = self.get_text(self.checkdata[13][0],self.checkdata[13][1])  #获取查看页面chatbotid文本值
        return vlaue

    def check_chatbot(self,result='0'):
        """
        开始审核chatbot
        :param result: 默认审核通过
        :return:
        """
        self.click_element(self.checkdata[7][0],self.checkdata[7][1])  #点击审核按钮

        if result=='0':   #审核通过
            chatbot_log.csp_log.info(f'{self.adddate[13][-1]} 审核通过')

        elif result !='0':  #审核不通过
            self.click_element(self.checkdata[8][0],self.checkdata[8][1])  #点击审核不通过
            self.wait(2)
            self.input_value(self.checkdata[9][0],self.checkdata[9][1],self.checkdata[9][2])  #输入审核不通过原因
            self.wait(2)


        self.click_element(self.checkdata[10][0],self.checkdata[10][1])  #点击确认审核
        self.wait(2)
        self.F5()

    def update_check_chatbot(self,update_result='0'):
        """
        更新chatbot审核
        :param update_result:
        :return:
        """
        self.click_element(self.checkdata[7][0], self.checkdata[7][1])  # 点击审核按钮
        if update_result=='0':   #审核通过
            chatbot_log.csp_log.info(f'{self.adddate[13][-1]} 信息变更审核通过')

        elif update_result !='0':  #审核不通过
            self.click_element(self.updatedata[10][0],self.updatedata[10][1])  #点击审核不通过
            self.wait(2)
            self.input_value(self.updatedata[11][0],self.updatedata[11][1],self.updatedata[11][2])  #输入审核不通过原因
            self.wait(2)


        self.click_element(self.updatedata[9][0],self.updatedata[9][1])  #点击确认审核
        self.wait(2)
        self.F5()


    def assert_chatbot_rate(self,chatbot_rate=updatedata[4][-1]):
        """
        变更Chatbot速率获取标签文本值
        :return:
        """
        rate = f'<div>{chatbot_rate}</div>'
        return rate





















