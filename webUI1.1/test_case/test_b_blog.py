from webUI.common.my_log import Log
from webUI.common.my_unit import MYunit
import logging
import unittest
from webUI.common import screenshoot
from webUI.Page.blog_page import BlogPage


testblog_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)



class Test_blog(MYunit):

    def test_a_newblog(self):
        """
        测试新建一个日志
        :return:
        """
        self.login.login()
        self.login.wait(5)

        self.blog = BlogPage(driver=self.driver)


        self.blog.new_blog()
        self.blog.wait(5)
        screenshoot.screen_shoot(self.driver,"blog_success")
        value = self.blog.blogtag[-1]
        value2 = self.blog.getpagecode()
        try:

            self.assertIn(value, value2)

        except Exception:
            testblog_log.action_log.exception(f'断言失败，案例不通过---------{value}不在当前页面')
            raise

        else:
            testblog_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value}在当前页面')

    def test_b_changeblog(self):
        """
        测试变更日志信息
        :return:
        """

        self.blog = BlogPage(driver=self.driver)
        self.blog.change_blog()

        screenshoot.screen_shoot(self.driver,"change_blog")
        value = self.blog.newtitle
        value2 = self.blog.getpagecode()
        try:

            self.assertIn(value, value2)

        except Exception:
            testblog_log.action_log.exception(f'断言失败，案例不通过---------{value}不在当前页面')
            raise

        else:
            testblog_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value}在当前页面')

    def test_c_deleteblog(self):
        """
        测试删除日志
        :return:
        """


        self.blog = BlogPage(driver=self.driver)
        self.blog.delete_blog()
        screenshoot.screen_shoot(self.driver,"delete_blog")
        value = self.blog.blogtag[-1]
        value2 = self.blog.getpagecode()
        try:

            self.assertNotIn(value, value2)

        except Exception:
            testblog_log.action_log.exception(f'断言失败，案例不通过---------{value}不在当前页面')
            raise

        else:
            testblog_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value}在当前页面')



if __name__=="__main__":
    unittest.main()