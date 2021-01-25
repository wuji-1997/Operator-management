from common.myunit import MYunit
from common.my_log import Log
import logging
import unittest
from Page.update_password_page import UpdatepwsPage
from common import screenshoot

updatepws_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

class Test_csp(MYunit):

    @unittest.skip('pass')
    def testcase01(self):
        """
        测试变更密码成功
        :return:
        """
        self.login.open()  #打开网站
        self.login.wait(2)

        self.updatepws = UpdatepwsPage(self.driver)
        self.updatepws.update_pws()
        self.updatepws.new_login()
        value = self.updatepws.get_url()
        value2 =self.updatepws.url
        screenshoot.screen_shoot(self.driver,r'\update_password','update_password')
        try:
            self.assertEqual(value, value2)
        except Exception:
            updatepws_log.csp_log.exception(f'Assertion Failed，case is not pass---------“{value}” is not equal to “{value2}”')
            raise
        else:
            updatepws_log.csp_log.info(f'Assertion Successed，case is  pass-----------“{value}” is equal to “{value2}”')


if __name__=="__main__":
    unittest.main()




