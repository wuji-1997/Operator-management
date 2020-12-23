from webUI.common.my_log import Log
from webUI.common.my_unit import MYunit
import logging
import unittest
from webUI.common import screenshoot


testlogin_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_login(MYunit):



    def test_a_wrong(self):
        """
        输入错误账号
        :return:
        """
        self.login.login(email=self.login.bademail)
        self.login.wait(5)
        screenshoot.screen_shoot(self.driver,"emailworng")

        value = self.login.getpagecode()
        value2 = '登录帐号错误，请重试'
        try:

            self.assertIn(value2,value)

        except Exception:
            testlogin_log.action_log.exception(f'断言失败，案例不通过---------{value2}不在当前页面')
            raise

        else:
            testlogin_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value2}在当前页面')

    def test_b_wrong(self):
        """
        输入错误密码
        :return:
        """
        self.login.login(pws=self.login.badpassword)
        self.login.wait(5)
        screenshoot.screen_shoot(self.driver,"passwordwrong")
        value = self.login.getpagecode()
        value2 = '用户密码错误!'
        try:

            self.assertIn(value2,value)

        except Exception:
            testlogin_log.action_log.exception(f'断言失败，案例不通过---------{value2}不在当前页面')
            raise

        else:
            testlogin_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value2}在当前页面')

    def test_c_null(self):
        """
        密码为空
        :return:
        """
        self.login.login(pws='')
        self.login.wait(5)
        screenshoot.screen_shoot(self.driver,"passwordnull")
        value = self.login.getpagecode()
        value2 = '密码不能为空!'
        try:

            self.assertIn(value2,value)

        except Exception:
            testlogin_log.action_log.exception(f'断言失败，案例不通过---------{value2}不在当前页面')
            raise

        else:
            testlogin_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value2}在当前页面')


    def test_z_login(self):
        """
        登录成功
        :return:
        """
        self.login.login()
        self.login.wait(5)
        screenshoot.screen_shoot(self.driver,"loginsuccess")
        value = self.login.get_url()
        try:

            self.assertEqual(value,'http://localhost/iwebsns/main.php')

        except Exception:
            testlogin_log.action_log.exception(f'断言失败，案例不通过---------{value}错误')
            raise

        else:
            testlogin_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value}')

if __name__=="__main__":
    unittest.main()