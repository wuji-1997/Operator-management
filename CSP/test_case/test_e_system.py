from common.myunit import MYunit
from common.my_log import Log
import logging
import unittest
from Page.system_management_page import SyStem_Management_Page
from common import screenshoot

test_system_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_system(MYunit):

    #@unittest.skip('pass')
    def testcase01(self):
        """
        测试新增一个账号
        :return:
        """
        self.login.csp_login()
        self.login.wait(2)
        self.system = SyStem_Management_Page(self.driver)

        self.system.add_user()
        self.system.intouser()
        self.system.find_user(username=self.system.accountdate[14][2],usernumber=self.system.accountdate[21][2],
                              usertype=self.system.accountdate[19][2],userstatus='启用')
        screenshoot.screen_shoot(self.driver,r'\system','新增账号')
        value = self.system.assert_text(text=self.system.accountdate[14][2])
        value2 =self.system.getpagecode()

        try:
            self.assertIn(value,value2)
        except Exception:
            test_system_log.csp_log.exception(f'Assertion Failed，case is not passed------{value} is not in page ')
            raise
        else:
            test_system_log.csp_log.info(f'Assertion Success，case is  passed------{value} is  in page ')

    #@unittest.skip('pass')
    def testcase02(self):
        """
        测试变更账号信息
        :return:
        """
        self.system = SyStem_Management_Page(self.driver)
        self.system.intouser()
        self.system.find_user(username=self.system.accountdate[14][2], usernumber=self.system.accountdate[21][2],
                              usertype=self.system.accountdate[19][2], userstatus='启用')
        self.system.update_user()
        self.system.F5()
        self.system.intouser()
        self.system.find_user(username=self.system.accountdate[9][2], usernumber=self.system.accountdate[21][2],
                              usertype=self.system.accountdate[19][2], userstatus='启用')
        screenshoot.screen_shoot(self.driver,'\system','变更账号信息')
        value = self.system.assert_text(text=self.system.accountdate[9][2])
        value2 = self.system.getpagecode()
        try:
            self.assertIn(value,value2)
        except Exception:
            test_system_log.csp_log.exception(f'Assertion Failed，case is not passed------{value} is not in page ')
            raise
        else:
            test_system_log.csp_log.info(f'Assertion Success，case is  passed------{value} is  in page ')

    def testcase03(self):
        """
        测试停用账号
        :return:
        """
        self.system = SyStem_Management_Page(self.driver)
        self.system.intouser()
        self.system.find_user(username=self.system.accountdate[9][2], usernumber=self.system.accountdate[21][2],
                              usertype=self.system.accountdate[19][2], userstatus='启用')

        self.system.stop_user()
        self.system.F5()
        self.system.intouser()
        self.system.find_user(username=self.system.accountdate[9][2], usernumber=self.system.accountdate[21][2],
                              usertype=self.system.accountdate[19][2], userstatus='禁用')

        screenshoot.screen_shoot(self.driver, '\system', '账号禁用')
        value = self.system.assert_text(text=self.system.accountdate[9][2])
        value2 = self.system.getpagecode()
        try:
            self.assertIn(value, value2)
        except Exception:
            test_system_log.csp_log.exception(f'Assertion Failed，case is not passed------{value} is not in page ')
            raise
        else:
            test_system_log.csp_log.info(f'Assertion Success，case is  passed------{value} is  in page ')

    def testcase04(self):
        """
        测试删除账号
        :return:
        """
        self.system = SyStem_Management_Page(self.driver)
        self.system.intouser()
        self.system.find_user(username=self.system.accountdate[9][2], usernumber=self.system.accountdate[21][2],
                              usertype=self.system.accountdate[19][2], userstatus='禁用')

        self.system.detele_user()
        self.system.F5()
        self.system.intouser()
        self.system.find_user(username=self.system.accountdate[9][2], usernumber=self.system.accountdate[21][2],
                              usertype=self.system.accountdate[19][2], userstatus='禁用')
        screenshoot.screen_shoot(self.driver, '\system', '删除账号')
        value = self.system.assert_text(text=self.system.accountdate[9][2])
        value2 = self.system.getpagecode()
        try:
            self.assertNotIn(value, value2)
        except Exception:
            test_system_log.csp_log.exception(f'Assertion Failed，case is not passed------{value} is  in page ')
            raise
        else:
            test_system_log.csp_log.info(f'Assertion Success，case is  passed------{value} is not in page ')


if __name__=="__main__":
    unittest.main()









