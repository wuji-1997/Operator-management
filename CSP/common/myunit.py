import unittest
import logging
from common.my_log import Log
from Page.login_page import LoginPage_CSP
from common.mydriver import Driver
myunit_log =Log(__name__,file=logging.INFO,cmd=logging.INFO)




class MYunit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """

        :return:
        """
        mydiver = Driver()
        cls.driver =mydiver.chormedriver()

        myunit_log.csp_log.info(f'Connection driver {cls.driver} success')

    def setUp(self):
        """

        :return:
        """
        self.login =LoginPage_CSP(driver=self.driver)


        myunit_log.csp_log.info('------------------starting  case-----------------')

    def tearDown(self):
        """

        :return:
        """
        self.driver.refresh()
        myunit_log.csp_log.info('------------------case completed-----------------')

    @classmethod
    def tearDownClass(cls):
        """

        :return:
        """
        cls.driver.quit()
        myunit_log.csp_log.info(f'break driver {cls.driver} SUCCESS')
