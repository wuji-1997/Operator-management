import unittest
import logging
from common.my_log import Log
from common.myunit import MYunit
from Page.chatbot_page import ChatbotPage
from common import screenshoot
import time
from common.writeexcel import Write_Excel
from config import Conf
test_cspchatbot_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)
writedata=Write_Excel(filepath=Conf.test_data+r'\test_chatbot_data.xlsx',number=4)

class Test_chatbot(MYunit):


    def testcase01(self):
        """
        测试新建一个chatbot且审核通过
        :return:
        """
        self.login.csp_login()
        self.login.wait(2)
        self.chatbot = ChatbotPage(self.driver)
        value = self.chatbot.assert_chatbotname()
        self.chatbot.add_chatbot()               #新增一个chatbot
        self.chatbot.intocheck()                 #进入chatbot审核内置表单
        self.chatbot.find_check()                #查询出待审核的chatbot数据
        value2 = self.chatbot.getpagecode()
        if value in value2:
            self.chatbot.check_chatbot()             #开始审核chatbot且审核通过
            self.chatbot.find_chatbot()              #管理节点再次查询出查询chatbot
            screenshoot.screen_shoot(self.driver,r'\chatbot','新增chatbot且审核通过')
            value3 = self.chatbot.getpagecode()
            try:
                self.assertIn(value, value3)
            except Exception:
                test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is not in page ')
                writedata.update_data(2,9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value} is  in page ')
                writedata.update_data(2,9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspchatbot_log.csp_log.exception(f'查询数据{self.chatbot.update_value[0]}失败')
                writedata.update_data(2, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise



    def testcase02(self):
        """
        测试新增一个chatbot且审核不通过
        :return:
        """
        self.chatbot = ChatbotPage(self.driver)
        checkname = self.chatbot.add_value[2]+'5'
        value = self.chatbot.assert_chatbotname(chatbot_name=checkname)
        self.chatbot.add_chatbot(name=checkname)  #新增一个chatbot
        self.chatbot.intocheck(way='2')                               #进入chatbot审核内置表单无需身份验证
        self.chatbot.find_check(check_chatbotname=checkname)       #查询出待审核的数据
        value2 = self.chatbot.getpagecode()
        if value in value2:
            self.chatbot.check_chatbot(result='2')  #审核不通过chatbot
            self.chatbot.find_chatbot(chatbotname=checkname)   #管理节点查询出chatbot数据
            value3 = self.chatbot.getpagecode()
            screenshoot.screen_shoot(self.driver,'\chatbot','新增chatbot审核不通过')
            self.chatbot.wait(2)
            try:
                self.assertNotIn(value, value3)
            except Exception:
                test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is  in page ')
                writedata.update_data(3,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value} is not in page ')
                writedata.update_data(3,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspchatbot_log.csp_log.exception(f'查询数据{self.chatbot.update_value[0]}失败')
                writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise


    def testcase03(self):
        """
        测试变更chatbot名称
        :return:
        """

        self.chatbot = ChatbotPage(self.driver)
        value2 = self.chatbot.assert_chatbotname()
        self.chatbot.find_chatbot()     #管理节点查询出chatbot数据
        value = self.chatbot.getpagecode()
        if value2 in value:
            self.chatbot.into_lookover()    #点击查看按钮进入查看页面
            self.chatbot.update_name()      #变更chatbot名称
            self.chatbot.intocheck(way='2')        #进入chatbot审核内置表单无需身份验证
            self.chatbot.find_check(check_type='信息变更')       #查询出待审核的chatbot数据
            value3 = self.chatbot.getpagecode()
            if value2 in value3:
                self.chatbot.check_chatbot()    #审核通过chatbot
                self.chatbot.find_chatbot(chatbotname=self.chatbot.update_value[0]) #查询出变更后的chatbot数据
                self.chatbot.wait(2)
                value5 = self.chatbot.getpagecode()
                screenshoot.screen_shoot(self.driver,'\chatbot','变更chatbot名称')
                value4 = self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.update_value[0])
                try:
                    self.assertIn(value4, value5)
                except Exception:
                    test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value4} is not in page ')
                    writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value4} is  in page ')
                    writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:

                text = False
                try:
                    self.assertTrue(text)
                except Exception:
                    test_cspchatbot_log.csp_log.exception('chatbot名称变更失败')
                    writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
        else:

            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspchatbot_log.csp_log.exception('查询的chatbot不存在')
                writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise

    def testcase04(self):
        """
        测试变更cahtbot配置
        :return:
        """
        self.chatbot = ChatbotPage(self.driver)
        self.chatbot.find_chatbot(chatbotname=self.chatbot.update_value[0])     #管理节点查询出chatbot数据
        value= self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.update_value[0])
        value2 = self.chatbot.getpagecode()
        if value in value2:
            self.chatbot.into_lookover()    #点击查看按钮进入查看页面
            self.chatbot.update_speed()     #变更chatbot速率
            self.chatbot.find_chatbot(chatbotname=self.chatbot.update_value[0])     #管理节点查询出chatbot数据
            self.chatbot.into_lookover()  # 点击查看按钮进入查看页面
            value4 = self.chatbot.getpagecode()
            screenshoot.screen_shoot(self.driver,'\chatbot','变更chatbot速率配置')
            value3=self.chatbot.assert_chatbot_rate()
            self.chatbot.wait(2)

            try:
                self.assertIn(value3,value4)
            except Exception:
                test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value3} is not in page ')
                writedata.update_data(5,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value3} is  in page ')
                writedata.update_data(5,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspchatbot_log.csp_log.exception('查询的chatbot不存在')
                writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise


    def testcase05(self):
        """
        测试注销第一个chatbot
        :return:
        """
        self.chatbot = ChatbotPage(self.driver)
        self.chatbot.find_chatbot(chatbotname=self.chatbot.update_value[0])            # 管理节点查询出chatbot数据
        value = self.chatbot.getpagecode()
        value2 =self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.update_value[0])
        if value2 in value:
            self.chatbot.into_lookover()           #点击查看按钮进入查看页面
            self.chatbot.delete_chatbot()          #注销chatbot
            self.chatbot.find_chatbot(chatbotname=self.chatbot.update_value[0])            # 管理节点查询出chatbot数据
            self.chatbot.wait(2)
            value3 = self.chatbot.getpagecode()
            screenshoot.screen_shoot(self.driver, '\chatbot','注销chatbot')
            try:
                self.assertNotIn(value2, value3)
            except Exception:
                test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value2} is  in page ')
                writedata.update_data(6,9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value2} is not in page ')
                writedata.update_data(6,9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspchatbot_log.csp_log.exception(f'查询数据{self.chatbot.update_value[0]}失败')
                writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise






if __name__=="__main__":
    unittest.main()