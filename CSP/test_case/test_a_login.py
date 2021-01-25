from common.myunit import MYunit
from common.my_log import Log
from common import screenshoot
import logging
import unittest


test_csplogin_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

class Test_csp(MYunit):



    def test_a_username_null(self):
        """
        测试账号为空
        :return:
        """
        self.login.open()
        self.login.user(email='')
        self.login.loginbutton()
        screenshoot.screen_shoot(self.driver, r'\login', 'csp_username_null')
        value = '账号不能为空。'
        value2 = self.login.getpagecode()
        try:
            self.assertIn(value, value2)
        except Exception:
            test_csplogin_log.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is not in page ')
            raise
        else:
            test_csplogin_log.csp_log.info(f'Assertion Successed，case is  pass---------{value} is  in page ')

    def test_b_userpassword_null(self):
        """
        测试密码为空
        :return:
        """
        self.login.user(pws='')
        self.login.loginbutton()
        screenshoot.screen_shoot(self.driver, r'\login', 'csp_userpws_null')
        value = '密码不能为空。'
        value2 = self.login.getpagecode()
        try:
            self.assertIn(value, value2)
        except Exception:
            test_csplogin_log.csp_log.exception(f'Assertion Failed，case is not pass---------“{value}” is not in page ')
            raise
        else:
            test_csplogin_log.csp_log.info(f'Assertion Successed，case is  pass---------“{value}” is  in page ')



    def test_c_photonull(self):
        """
        测试图形验证码为空
        :return:
        """
        self.login.user()
        self.login.loginbutton()
        screenshoot.screen_shoot(self.driver,r'\login','csp_photo_null')
        value = '图形验证码不能为空。'
        value2 =self.login.getpagecode()
        try:
            self.assertIn(value,value2)
        except Exception:
            test_csplogin_log.csp_log.exception(f'Assertion Failed，case is not pass---------“{value}” is not in page ')
            raise
        else:
            test_csplogin_log.csp_log.info(f'Assertion Successed，case is  pass---------“{value}” is  in page ')

    def test_d_msgnull(self):
        """
        测试手机短信码为空
        :return:
        """

        self.login.user()
        self.login.clickphoto()
        self.login.loginbutton()
        screenshoot.screen_shoot(self.driver,r'\login','csp_msg_null')
        value = '短信验证码不能为空。'
        value2 =self.login.getpagecode()
        try:
            self.assertIn(value, value2)
        except Exception:
            test_csplogin_log.csp_log.exception(f'Assertion Failed，case is not pass---------“{value}” is not in page ')
            raise
        else:
            test_csplogin_log.csp_log.info(f'Assertion Successed，case is  pass---------“{value}” is  in page ')

    def test_e_csplogin(self):
        """
        测试登录成功
        :return:
        """

        self.login.csp_login()
        self.login.wait(2)
        screenshoot.screen_shoot(self.driver,r'\login','csp_login')
        value = self.login.url
        value2 = self.login.get_url()
        try:
            self.assertEqual(value, value2)
        except Exception:
            test_csplogin_log.csp_log.exception(f'Assertion Failed，case is not pass---------“{value}” is not equal to “{value2}”')
            raise
        else:
            test_csplogin_log.csp_log.info(f'Assertion Successed，case is  pass-----------“{value}” is equal to “{value2}”')

if __name__=="__main__":
    unittest.main()

