from common.my_log import Log
from common.myunit import MYunit
import logging
import unittest
from Page.csp_page.customer_page import CustmoerPage
from common import screenshoot
from common.writeexcel import Write_Excel
import time
from config import Conf
test_cspcustmoer_log = Log(__name__,file=logging.INFO,cmd=logging.WARN)
writedata=Write_Excel(filepath=Conf.test_data+r'\test_customer_data.xlsx',number=4)

class Test_csp_custmoer(MYunit):


    def testcase01(self):
        """
        测试新增客户且审核通过
        :return:
        """
        self.login.csp_login()
        self.login.wait(0.5)
        self.custmoer = CustmoerPage(self.driver)
        value = self.custmoer.assert_text(self.custmoer.add_value[0])
        self.custmoer.add_customer()  # 新建客户
        self.custmoer.finding_check(way_number=True)  # 需身份验证查询待审核的数据
        value2 = self.custmoer.getpagecode()
        if value in value2:
            self.custmoer.click_check()  # 客户信息新建审核通过
            self.custmoer.find_name()  # 查询数据
            screenshoot.screen_shoot(self.driver, r'\customer', '新增客户审核通过')
            value3 = self.custmoer.getpagecode()
            try:
                self.assertIn(value,value3)
            except Exception:
                test_cspcustmoer_log.csp_log.exception(f'断言失败，案例--testcase02不通过-----{value} 不在当前页面')
                writedata.update_data(2,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                test_cspcustmoer_log.csp_log.info(f'断言成功，案例--testcase02通过------{value} 在当前页面')
                writedata.update_data(2,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")

        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspcustmoer_log.csp_log.exception(f'未查询到待审核的数据----{self.custmoer.add_value[0]}--------请重新调试案例')
                writedata.update_data(2, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise

    #@unittest.skip('pass')
    def testcase02(self):
        """
        测试新增客户审核不通过
        :return:
        """

        self.custmoer = CustmoerPage(self.driver)
        new_name = self.custmoer.random_number()
        value = self.custmoer.assert_text(text=new_name)
        self.custmoer.add_customer(name=new_name,number='18360766327')  # 新建客户
        self.custmoer.finding_check(way_number=False

                                    ,checkname=new_name)      #无需身份验证查询待审核的数据
        value2 = self.custmoer.getpagecode()
        if value in value2:
            self.custmoer.click_check(result='1')            #客户信息新建审核不通过
            self.custmoer.find_name(customername=new_name)                        #查询数据
            screenshoot.screen_shoot(self.driver, r'\customer', '新增客户审核不通过')
            value3 =self.custmoer.getpagecode()
            try:
               self.assertNotIn(value,value3)
            except Exception:
               writedata.update_data(3,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
               test_cspcustmoer_log.csp_log.exception(f'断言失败，案例--testcase02不通过-----{value} 在当前页面')
               raise
            else:
               test_cspcustmoer_log.csp_log.info(f'断言成功，案例--testcase02通过------{value} 不在当前页面---审核通过')
               writedata.update_data(3,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspcustmoer_log.csp_log.exception(f'未查询到待审核的数据----{self.custmoer.add_value[0]}--------请重新调试案例')
                writedata.update_data(3,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise

    #@unittest.skip('pass')
    def testcase03(self):
        """
        测试变更客户名称
        :return:
        """

        self.custmoer = CustmoerPage(self.driver)
        if self.custmoer.assert_find(findname=self.custmoer.search[4],asserttext=self.custmoer.search[4]):
            self.custmoer.update_msg()   #进入查看页面变更客户名称
            self.custmoer.finding_check(way_number=False,checkname=self.custmoer.search[4],check_way='信息变更')  # 无需身份验证查询待审核的数据
            self.custmoer.click_check()  # 变更审核通过
            self.custmoer.find_name(customername=self.custmoer.update_user[3])  #查询出新的客户名
            screenshoot.screen_shoot(self.driver,r'\customer','客户名称变更')
            value3 = self.custmoer.getpagecode()
            value4 = self.custmoer.assert_text(text=self.custmoer.update_user[3])

            try:
                self.assertIn(value4, value3)
            except Exception:
                writedata.update_data(4,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                test_cspcustmoer_log.csp_log.exception(f'断言失败，案例不通过---客户信息变更失败')
                raise
            else:
                test_cspcustmoer_log.csp_log.info(f'断言成功，案例--案例通过---客户名称由“{self.custmoer.search[4]}”变更为{self.custmoer.update_user[3]}')
                writedata.update_data(4,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspcustmoer_log.csp_log.exception(f'未查询到待审核的数据----{self.custmoer.search[4]}--------请重新调试案例')
                writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise


    def testcase04(self):
        """
        测试变更客户归属csp
        :return:
        """

        self.custmoer = CustmoerPage(self.driver)
        value4 = self.custmoer.assert_text(text=self.custmoer.update_user[3])

        if self.custmoer.assert_find(findname=self.custmoer.update_user[3], asserttext=self.custmoer.update_user[3]):
            self.custmoer.update_csp()
            self.custmoer.finding_check(way_number=False, checkname=self.custmoer.update_user[3],check_way='信息变更')  # 无需身份验证查询待审核的数据
            self.custmoer.click_check()  # 变更审核通过
            self.custmoer.find_name(customername=self.custmoer.update_user[3],belog_csp=self.custmoer.update_user[4],customer_type=self.custmoer.update_user[5])
            screenshoot.screen_shoot(self.driver, r'\customer', '客户归属csp变更')
            value3 = self.custmoer.getpagecode()

            try:
                self.assertIn(value4, value3)
            except Exception:
                writedata.update_data(5,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                test_cspcustmoer_log.csp_log.exception(f'断言失败，案例不通过---客户信息变更失败')
                raise
            else:
                test_cspcustmoer_log.csp_log.info(f'断言成功，案例--案例通过---客户归属csp由“{self.custmoer.check[4]}”变更为{self.custmoer.update_user[5]}')
                writedata.update_data(5,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")

        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                    test_cspcustmoer_log.csp_log.exception(f'未查询到待审核的数据----{self.custmoer.update_user[3]}--------请重新调试案例')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise


    #@unittest.skip('pass')
    def testcase05(self):
        """
        测试删除客户
        :return:
        """
        self.custmoer = CustmoerPage(self.driver)
        value =self.custmoer.assert_text(text=self.custmoer.add_value[24])
        if self.custmoer.assert_find(findname=self.custmoer.add_value[24],asserttext=value):
           self.custmoer.delete_user()                            #进入查看客户信息页面操作注销该客户
           self.custmoer.find_name(customername=self.custmoer.add_value[24])  #查询已经审核通过的客户数据
           screenshoot.screen_shoot(self.driver, r'\customer','删除客户')
           self.custmoer.wait(0.5)
           value3 =self.custmoer.getpagecode()
           try:
               self.assertNotIn(value,value3)
           except Exception:
               writedata.update_data(5,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
               test_cspcustmoer_log.csp_log.exception(f'断言失败，案例不通过---删除失败')
               raise
           else:
               test_cspcustmoer_log.csp_log.info(f'断言成功，案例--案例通过---删除成功')
               writedata.update_data(5,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_cspcustmoer_log.csp_log.exception(f'未查询到待删除的数据----{self.custmoer.add_value[0]}--------请重新调试案例'
                                                       f'原因可能是案例一失败')
                writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
    #@unittest.skip('pass')
    def testcase06rename(self):
        """
        测试还原
        :return:
        """

        self.custmoer = CustmoerPage(self.driver)
        self.custmoer.find_name(customername=self.custmoer.update_user[3],belog_csp=self.custmoer.update_user[4],
                                customer_type=self.custmoer.update_user[5],)  # 查询出待变更的数据
        self.custmoer.refresh()
        self.custmoer.finding_check(way_number=False,checkname=self.custmoer.update_user[3], check_way='信息变更',
                                    type=self.custmoer.search[2][15],number='1')  # 无需身份验证查询待审核的数据
        self.custmoer.click_check(number='1')  # 变更审核通过
        self.custmoer.find_name(customername=self.custmoer.search[4])
        value = self.custmoer.assert_text(text=self.custmoer.search[4])
        value2=self.custmoer.getpagecode()
        try:
            self.assertIn(value,value2)
        except Exception:
            test_cspcustmoer_log.csp_log.exception(f'客户名称变更为{self.custmoer.search[4]}失败')
            raise
        else:
            test_cspcustmoer_log.csp_log.info(f'客户名称变更为{self.custmoer.search[4]}成功')




if __name__=="__main__":
    unittest.main()


