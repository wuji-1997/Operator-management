from common.my_log import Log
from common.myunit import MYunit
import logging
import unittest
from Page.customer_page import CustmoerPage
from common import screenshoot
test_cspcustmoer_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

class Test_csp_custmoer(MYunit):


    def testcase01(self):
        """
        测试是否新建成功一个用户
        :return:
        """
        self.login.csp_login()
        self.login.wait(2)            #登录
        self.custmoer = CustmoerPage(self.driver)
        self.custmoer.add_customer()  #新建客户
        self.custmoer.finding_check()  #查询待审核的数据
        screenshoot.screen_shoot(self.driver,r'\customer','新增客户')
        value = self.custmoer.get_find_check_text()     #获取审核节点查询的数据客户名称字段文本值

        try:
            self.assertEqual(value,self.custmoer.add[1][-1])
        except Exception:
            test_cspcustmoer_log.csp_log.exception(f'断言失败，案例---testcase01不通过------------新建客户失败')
            raise
        else:
            test_cspcustmoer_log.csp_log.info(f'断言成功，案例---testcase01通过-------------新建客户成功')


    def testcase02(self):
        """
        测试新增客户审核不通过
        :return:
        """
        self.custmoer = CustmoerPage(self.driver)
        self.custmoer.finding_check(way_number='1')      #无需身份验证查询待审核的数据
        self.custmoer.click_check(result='1')            #客户信息新建审核不通过
        self.custmoer.find_name()                        #查询数据
        value2 =self.custmoer.getpagecode()
        value = f'<td>{self.custmoer.add[1][-1]}</td>'
        self.custmoer.wait(2)
        screenshoot.screen_shoot(self.driver, r'\customer', '新增客户审核不通过')
        try:
            self.assertNotIn(value,value2)
        except Exception:
            test_cspcustmoer_log.csp_log.exception(f'断言失败，案例--testcase02不通过-----{value} 在当前页面')
            raise
        else:
            test_cspcustmoer_log.csp_log.info(f'断言成功，案例--testcase02通过------{value} 不在当前页面----审核不通过-----查不到该数据')


    def testcase03(self):
        """
        测试新增客户审核通过
        :return:
        """
        self.custmoer = CustmoerPage(self.driver)
        self.custmoer.add_customer(name=self.custmoer.add[28])            #新建第二个客户
        self.custmoer.finding_check(checkname=self.custmoer.add[28],way_number='1')   #查询待审核的数据且无需验证身份
        self.custmoer.click_check(result='0')                                       #审核通过
        self.custmoer.find_name(customername=self.custmoer.add[28])                #查询数据
        value = self.custmoer.get_user_text()                                    #查询出数据获取客户名称文本值
        self.custmoer.wait(2)
        screenshoot.screen_shoot(self.driver,r'\customer','新增客户审核通过')
        value2 = self.custmoer.add[28]
        try:
            self.assertEqual(value,value2)
        except Exception:
            test_cspcustmoer_log.csp_log.exception(f'断言失败，案例--testcase03不通过---------{value} =!{value2},审核失败，新建客户失败')
            raise
        else:
            test_cspcustmoer_log.csp_log.info(f'断言成功，案例--testcase03通过-----------{value} ={value2} 审核成功，新建客户成功')


    def testcase04(self):
        """
        测试删除客户
        :return:
        """
        self.custmoer = CustmoerPage(self.driver)
        self.custmoer.find_name(customername=self.custmoer.add[28])    #查询已经审核通过的客户数据
        value = self.custmoer.delete_user()                            #进入查看客户信息页面操作注销该客户
        self.custmoer.find_name(customername=self.custmoer.add[28])
        value2 = self.custmoer.getpagecode()
        screenshoot.screen_shoot(self.driver,r'\customer','删除客户')
        try:
            self.assertNotIn(value,value2)
        except Exception:
            test_cspcustmoer_log.csp_log.exception(f'断言失败，案例--testcase04不通过---删除失败---可以查询到编码为{value}的客户')
            raise
        else:
            test_cspcustmoer_log.csp_log.info(f'断言成功，案例--testcase04通过---删除成功---无法查询到编码为{value}的客户')








if __name__=="__main__":
    unittest.main()


