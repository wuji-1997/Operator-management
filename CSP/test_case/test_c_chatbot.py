import unittest
import logging
from common.my_log import Log
from common.myunit import MYunit
from Page.chatbot_page import ChatbotPage
from common import screenshoot

test_cspchatbot_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_chatbot(MYunit):


    def testcase01(self):
        """
        测试新建一个chatbot
        :return:
        """
        self.login.csp_login()
        self.login.wait(2)
        self.chatbot = ChatbotPage(self.driver)
        self.chatbot.add_chatbot() #新增一个chatbot
        self.chatbot.intocheck()  #进入chatbot审核内置表单
        self.chatbot.find_check()  #查询出待审核的chatbot数据
        screenshoot.screen_shoot(self.driver, '\chatbot', 'add_chatbot')
        value=self.chatbot.assert_chatbotname()
        self.chatbot.wait(1)
        value2 =self.chatbot.getpagecode()
        try:
            self.assertIn(value, value2)
        except Exception:
            test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is not in page ')
            raise
        else:
            test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value} is  in page ')


    def testcase02(self):
        """
        测试新增一个chatbot且审核通过
        :return:
        """

        self.chatbot = ChatbotPage(self.driver)
        self.chatbot.intocheck(way='2')  # 进入chatbot审核内置表单无需身份验证
        self.chatbot.find_check()     #查询出待审核的数据
        self.chatbot.check_chatbot()  #审核通过chatbot
        self.chatbot.find_chatbot()   #管理节点查询出chatbot数据
        screenshoot.screen_shoot(self.driver,'\chatbot','chatbot_passed')
        value = self.chatbot.assert_chatbotname()
        self.chatbot.wait(2)
        value2 = self.chatbot.getpagecode()
        try:
            self.assertIn(value, value2)
        except Exception:
            test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is not in page ')
            raise
        else:
            test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value} is  in page ')


    def testcase03(self):
        """
        测试新增一个chatbot且审核不通过
        :return:
        """
        self.chatbot = ChatbotPage(self.driver)
        self.chatbot.add_chatbot(name=self.chatbot.adddate[34])
        self.chatbot.intocheck(way='2')  # 进入chatbot审核内置表单无需审核
        self.chatbot.find_check(check_chatbotname=self.chatbot.adddate[34])   #查询出待审核的数据
        self.chatbot.check_chatbot(result='1')  #查询出待审核的数据且审核chatbot不通过
        self.chatbot.find_chatbot(chatbotname=self.chatbot.adddate[34])  # 管理节点查询出chatbot数据
        screenshoot.screen_shoot(self.driver, '\chatbot', 'chatbot_not_passed')
        value = self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.adddate[34])
        self.chatbot.wait(2)
        value2 = self.chatbot.getpagecode()
        try:
            self.assertNotIn(value, value2)
        except Exception:
            test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is  in page ')
            raise
        else:
            test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value} is not in page ')


    def testcase04(self):
        """
        测试变更chatbot名称
        :return:
        """
        self.chatbot = ChatbotPage(self.driver)
        self.chatbot.find_chatbot()  # 管理节点查询出chatbot数据
        self.chatbot.into_lookover(code='2')  #点击查看按钮进入查看页面
        self.chatbot.update_chatbot()   #变更chatbot名称

        self.chatbot.intocheck(way='2')  # 进入chatbot审核内置表单无需身份验证
        self.chatbot.find_check()  # 查询出待审核的chatbot数据
        self.chatbot.update_check_chatbot()  # 审核通过chatbot
        self.chatbot.find_chatbot(chatbotname=self.chatbot.new_chatbot) #查询出变更后的chatbot数据
        screenshoot.screen_shoot(self.driver,'\chatbot','update_cahtbot_name')
        value = self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.new_chatbot)
        self.chatbot.wait(2)
        value2 = self.chatbot.getpagecode()
        try:
            self.assertIn(value, value2)
        except Exception:
            test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is not in page ')
            raise
        else:
            test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value} is  in page ')


    def testcase05(self):
        """
        测试变更cahtbot配置
        :return:
        """
        self.chatbot = ChatbotPage(self.driver)
        self.chatbot.find_chatbot(chatbotname=self.chatbot.new_chatbot)  # 管理节点查询出chatbot数据
        self.chatbot.into_lookover(code='2')  # 点击查看按钮进入查看页面
        self.chatbot.update_chatbot(update_msg='1')  #变更chatbot速率
        self.chatbot.find_chatbot(chatbotname=self.chatbot.new_chatbot)  # 管理节点查询出chatbot数据
        self.chatbot.into_lookover(code='2')  # 点击查看按钮进入查看页面
        screenshoot.screen_shoot(self.driver,'\chatbot','update_chatbot_rate')
        value=self.chatbot.assert_chatbot_rate()
        self.chatbot.wait(2)
        value2 = self.chatbot.getpagecode()
        try:
            self.assertIn(value, value2)
        except Exception:
            test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is not in page ')
            raise
        else:
            test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value} is  in page ')


    def testcase06(self):
        """
        测试注销chatbot
        :return:
        """
        self.chatbot = ChatbotPage(self.driver)
        self.chatbot.find_chatbot()  # 管理节点查询出chatbot数据
        self.chatbot.into_lookover(code='2')  # 点击查看按钮进入查看页面
        self.chatbot.delete_chatbot()  #注销chatbot
        self.chatbot.find_chatbot()  # 管理节点查询出chatbot数据
        screenshoot.screen_shoot(self.driver, '\chatbot','delete_chatbot')
        value = self.chatbot.assert_chatbotname()
        self.chatbot.wait(2)
        value2 = self.chatbot.getpagecode()
        try:
            self.assertNotIn(value, value2)
        except Exception:
            test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is  in page ')
            raise
        else:
            test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value} is not in page ')









if __name__=="__main__":
    unittest.main()