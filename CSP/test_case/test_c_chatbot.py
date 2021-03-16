import unittest
import logging
from common.my_log import Log
from common.myunit import MYunit
from Page.csp_page.chatbot_page import ChatbotPage
from common import screenshoot
import time
from common.writeexcel import Write_Excel
from config import Conf
test_cspchatbot_log = Log(__name__,file=logging.INFO,cmd=logging.WARN)
writedata=Write_Excel(filepath=Conf.test_data+r'\test_chatbot_data.xlsx',number=4)

class Test_csp_chatbot(MYunit):

    #@unittest.skip('pass')
    def testcase01(self):
        """
        测试新建一个chatbot且审核通过
        :return:
        """
        self.login.csp_login()
        self.login.wait(0.5)
        self.chatbot = ChatbotPage(self.driver)
        value = self.chatbot.assert_chatbotname()
        self.chatbot.add_chatbot()               #新增一个chatbot
        self.chatbot.intocheck(way=True)         #进入chatbot审核内置表单
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

    #@unittest.skip('pass')
    def testcase02(self):
        """
        测试新增一个chatbot且审核不通过
        :return:
        """

        self.chatbot = ChatbotPage(self.driver)
        checkname =self.chatbot.random_number()
        value = self.chatbot.assert_chatbotname(chatbot_name=checkname)
        self.chatbot.add_chatbot(name=checkname)  #新增一个chatbot
        self.chatbot.intocheck(way=False)                               #进入chatbot审核内置表单无需身份验证
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
                test_cspchatbot_log.csp_log.exception(f'查询数据{checkname}失败')
                writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise

    #@unittest.skip('pass')
    def testcase03(self):
        """
        测试变更chatbot多个信息审核不通过
        :return:
        """

        self.chatbot = ChatbotPage(self.driver)
        value2 = self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.other)
        if self.chatbot.assert_find(findname=self.chatbot.other,assert_text=value2):
           self.chatbot.into_lookover()    #点击查看按钮进入查看页面
           self.chatbot.update_name()      #变更chatbot信息
           self.chatbot.intocheck(way=False)        #进入chatbot审核内置表单无需身份验证
           self.chatbot.find_check(check_chatbotname=self.chatbot.other,check_type='信息变更')       #查询出待审核的chatbot数据
           value3 = self.chatbot.getpagecode()
           if value2 in value3:
              self.chatbot.check_chatbot(result='10',check_way=self.chatbot.checkdata[2][15])    #审核不通过chatbot
              self.chatbot.find_chatbot(chatbotname=self.chatbot.update_value[0]) #查询出变更后的chatbot数据
              self.chatbot.wait(2)
              value5 = self.chatbot.getpagecode()
              screenshoot.screen_shoot(self.driver,'\chatbot','变更chatbot名称')
              value4 = self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.update_value[0])
              try:
                  self.assertNotIn(value4, value5)
              except Exception:
                  test_cspchatbot_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value4} is  in page ')
                  writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                  raise
              else:
                  test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value4} is NOT in page ')
                  writedata.update_data(4,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
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
        测试变更chatbot归属csp与客户
        :return:
        """

        self.chatbot = ChatbotPage(self.driver)
        value2 = self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.other)
        if self.chatbot.assert_find(findname=self.chatbot.other, assert_text=value2):
            self.chatbot.into_lookover()  # 点击查看按钮进入查看页面
            self.chatbot.update_csp()     #变更归属csp
            self.chatbot.intocheck(way=False)  # 进入chatbot审核内置表单无需身份验证
            self.chatbot.find_check(check_chatbotname=self.chatbot.other, check_type='信息变更')  # 查询出待审核的chatbot数据
            value3 = self.chatbot.getpagecode()
            if value2 in value3:
                self.chatbot.check_chatbot()  # 审核通过chatbot
                self.chatbot.find_update_chatbot()   #查询变更后的chatbot
                code=self.chatbot.getpagecode()
                screenshoot.screen_shoot(self.driver, '\chatbot', '变更chatbot归属csp与客户')
                try:
                    self.assertIn(value2,code)
                except Exception:
                    test_cspchatbot_log.csp_log.exception(
                        f'Assertion Failed，case is not pass---------{value2} is NOT in page ')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    test_cspchatbot_log.csp_log.info(
                        f'Assertion Successed，case is  pass---------{value2} is  in page ')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            else:
                text = False
                try:
                    self.assertTrue(text)
                except Exception:
                    test_cspchatbot_log.csp_log.exception('chatbot归属csp与客户变更失败')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
        else:

            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspchatbot_log.csp_log.exception('查询的chatbot不存在')
                writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise

    @unittest.skip('pass')
    def testcase05(self):
        """
        测试变更cahtbot配置
        :return:
        """

        self.chatbot = ChatbotPage(self.driver)
        value= self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.update_value[0])
        if  self.chatbot.assert_find(findname=self.chatbot.update_value[0],assert_text=value):
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

    #@unittest.skip('pass')
    def testcase06(self):
        """
        测试注销chatbot
        :return:
        """

        self.chatbot = ChatbotPage(self.driver)
        value2 = self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.add_value[15])
        if  self.chatbot.assert_find(findname=self.chatbot.add_value[15],assert_text=value2):
            self.chatbot.into_lookover()           #点击查看按钮进入查看页面
            self.chatbot.delete_chatbot()          #注销chatbot
            self.chatbot.find_chatbot(chatbotname=self.chatbot.add_value[15])            # 管理节点查询出chatbot数据
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

    @unittest.skip('pass')
    def testcase07_refreshspeed(self):
        """
        复原chatbot配置
        :return:
        """
        self.chatbot = ChatbotPage(self.driver)
        value2 = self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.other)
        value3 = self.chatbot.assert_chatbot_rate(chatbot_rate='50')
        if self.chatbot.assert_find(findname=self.chatbot.other,assert_text=value2):
            self.chatbot.into_lookover()  # 点击查看按钮进入查看页面
            self.chatbot.update_speed(speed='50')  # 变更chatbot速率
            self.chatbot.find_chatbot(chatbotname=self.chatbot.other)  # 查询chatbot
            self.chatbot.into_lookover()
            value4 = self.chatbot.getpagecode()
            screenshoot.screen_shoot(self.driver, '\chatbot', '变更chatbot速率配置')
            try:
                self.assertIn(value3, value4)
            except Exception:
                test_cspchatbot_log.csp_log.exception(
                    f'Assertion Failed，case is not pass---------{value3} is not in page ')
                raise
            else:
                test_cspchatbot_log.csp_log.info(f'Assertion Successed，case is  pass---------{value3} is  in page ')
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspchatbot_log.csp_log.exception('查询的chatbot不存在')
                raise

    def testcase08_refresh(self):
        """
        测试复原数据
        :return:
        """
        self.chatbot = ChatbotPage(self.driver)
        value2 = self.chatbot.assert_chatbotname(chatbot_name=self.chatbot.other)
        if self.chatbot.assert_find(findname=self.chatbot.other, assert_text=value2,assert_type='集团CSP'):
            self.chatbot.into_lookover()  # 点击查看按钮进入查看页面
            self.chatbot.update_csp(updatecsp=self.chatbot.add_value[0],updatecustomer=self.chatbot.add_value[1])  # 变更归属csp
            self.chatbot.intocheck(way=False)  # 进入chatbot审核内置表单无需身份验证
            self.chatbot.find_check(check_chatbotname=self.chatbot.other, check_type='信息变更',csp_type='集团CSP')  # 查询出待审核的chatbot数据
            value3 = self.chatbot.getpagecode()
            if value2 in value3:
                self.chatbot.check_chatbot()  # 审核通过chatbot
                self.chatbot.find_update_chatbot(chatbotcsp=self.chatbot.add_value[0],chatbotcustomer=self.chatbot.add_value[1])  # 查询变更后的chatbot
                code = self.chatbot.getpagecode()
                screenshoot.screen_shoot(self.driver, '\chatbot', '变更chatbot归属csp与客户')
                try:
                    self.assertIn(value2, code)
                except Exception:
                    test_cspchatbot_log.csp_log.exception(
                        f'Assertion Failed，case is not pass---------{value2} is NOT in page ')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    test_cspchatbot_log.csp_log.info(
                        f'Assertion Successed，case is  pass---------{value2} is  in page ')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            else:
                text = False
                try:
                    self.assertTrue(text)
                except Exception:
                    test_cspchatbot_log.csp_log.exception('chatbot归属csp与客户变更失败')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
        else:

            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspchatbot_log.csp_log.exception('查询的chatbot不存在')
                writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise



if __name__=="__main__":
    unittest.main()