import unittest
import logging
from webUI.common.my_log import Log
from webUI.Page.login_page import LoginPage
from webUI.common.driver import Getdriver
myunit_log =Log(__name__,file=logging.INFO,cmd=logging.INFO)



class MYunit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """

        :return:
        """
        cls.driver = Getdriver().usechorme()
        cls.driver.maximize_window()

        myunit_log.action_log.info(f'连接驱动{cls.driver}成功')

    def setUp(self) -> None:
        """

        :return:
        """
        self.login = LoginPage(driver=self.driver)
        self.login.open()
        myunit_log.action_log.info('------------------执行案例开始-----------------')

    def tearDown(self) -> None:
        """

        :return:
        """
        self.driver.refresh()
        myunit_log.action_log.info('------------------执行案例完成-----------------')

    @classmethod
    def tearDownClass(cls) -> None:
        """

        :return:
        """
        cls.driver.quit()
        myunit_log.action_log.info(f'断开驱动{cls.driver}成功')



