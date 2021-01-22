from common.myunit import MYunit
from common.my_log import Log
import logging
import unittest
from Page.csp_page import CspPage
from common.write_text import Text_action
from common import screenshoot
from config import Conf

csp_testlog = Log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_csp(MYunit):


    @unittest.skip('pass')
    def testcase01(self):
        """
        测试新增CSP
        :return:
        """
        self.login.csp_login()
        self.login.wait(2)
        self.csp = CspPage(self.driver)
        self.csp.new_csp()    #新增一个csp
        self.csp.intocheck()  #进入csp审核节点
        self.csp.find_check_csp()   #查询待审核的csp数据
        screenshoot.screen_shoot(self.driver,r'\csp','new_csp')
        value2 = self.csp.getpagecode()
        value=self.csp.get_assert_text()
        try:
            self.assertIn(value, value2)
        except Exception:
            csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------新建csp{self.csp.add[1][-1]}失败--{value} is not in page ')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  passed---------新建csp{self.csp.add[1][-1]}成功--{value} in page')

    @unittest.skip('pass')
    def testcase02(self):
        """
        测试审核创建csp的流程且审核通过
        :return:
        """

        self.csp = CspPage(self.driver)
        self.csp.intocheck(way='10')      #进入csp审核节点
        self.csp.find_check_csp() #查询出待审核的数据
        self.csp.starting_check()  #csp审核通过
        self.csp.find_csp_data()   #进入管理节点查询出已经通过审核的数据数据
        screenshoot.screen_shoot(self.driver,r'\csp','check_csp')
        value2=self.csp.getpagecode()
        value =self.csp.get_assert_text()
        try:
            self.assertIn(value,value2)
        except Exception:
            csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------csp审核失败--{value} is not in page')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp审核成功--{value} in page ')

    @unittest.skip('pass')
    def testcase03(self):
        """
        测试客户变更审核不通过
        :return:
        """

        self.csp = CspPage(self.driver)
        self.csp.find_csp_data()  # 进入管理页面查询出审核通过的csp数据
        self.csp.look_csp_data()  # 点击查看按钮
        self.csp.update_csp('1')  # 点击编辑按钮更新客户类型
        self.csp.intocheck(way='10')  # 进入审核内置表单
        self.csp.find_check_csp()  # 查询出待审核的数据
        self.csp.starting_check(result='10')  # 审核不通过
        self.csp.find_csp_data()  # 查询出数据
        self.csp.look_csp_data()  # 进入查看csp信息页面
        value2 = self.csp.getpagecode()
        value = self.csp.get_assert_look_text(element_text=self.csp.update[1][-1])
        screenshoot.screen_shoot(self.driver, r'\csp', 'update_csp_customertype_fail')

        try:
            self.assertNotIn(value, value2)
        except Exception:
            csp_testlog.csp_log.exception(
                f'Assertion Failed，case is not pass---------csp客户类型变更审核失败--{value}  in page ')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  pass-----csp客户类型变更审核不通过成功--{value} is not in page')

    @unittest.skip('pass')
    def testcase04(self):
        """
        测试更新csp客户类型且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        self.csp.find_csp_data()  #进入管理页面查询出审核通过的csp数据
        self.csp.look_csp_data()   #点击查看按钮
        self.csp.update_csp('1') #点击编辑按钮更新客户类型
        self.csp.intocheck(way='10')        #进入审核内置表单
        self.csp.find_check_csp()   #查询出待审核的数据
        self.csp.starting_check()   #审核通过
        self.csp.find_csp_data()    #查询出数据
        self.csp.look_csp_data()    #进入查看csp信息页面
        value2 = self.csp.getpagecode()
        value =self.csp.get_assert_look_text(element_text=self.csp.update[1][-1])
        screenshoot.screen_shoot(self.driver,r'\csp','update_csp_customertype_success')

        try:
            self.assertIn(value,value2)
        except Exception:
            csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------csp客户类型变更失败--{value} is not in page ')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp客户类型变更成功--{value} in page ')

    @unittest.skip('pass')
    def testcase05(self):
        """
        测试更新csp类型且审核不通过
        :return:
        """
        self.csp = CspPage(self.driver)
        self.csp.find_csp_data()  # 查询出数据
        self.csp.look_csp_data()  # 进入查看页面
        self.csp.update_csp('2')  # 更新csp类型
        self.csp.intocheck(way='10')  # 进入审核内置表单
        self.csp.find_check_csp()  # 查询出待审核的数据
        self.csp.starting_check(result='10')  # 审核不通过
        self.csp.find_csp_data(csp_type=self.csp.update[2][-1])  # 查询出数据
        value2 = self.csp.getpagecode()
        screenshoot.screen_shoot(self.driver, r'\csp', 'update_csp_type_fail')
        value = self.csp.get_assert_text()

        try:
            self.assertNotIn(value,value2)
        except Exception:
            csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------csp类型变更审核失败--{value}  in page ')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp类型变更审核不通过成功--{value} is not in page ')

    @unittest.skip('pass')
    def testcase06(self):
        """
        测试更新csp类型且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        self.csp.find_csp_data()  # 查询出数据
        self.csp.look_csp_data()  # 进入查看页面
        self.csp.update_csp('2')  # 更新csp类型
        self.csp.intocheck(way='10')  # 进入审核内置表单
        self.csp.find_check_csp()  # 查询出待审核的数据
        self.csp.starting_check()  # 审核通过
        self.csp.find_csp_data(csp_type=self.csp.update[2][-1])  # 查询出数据
        value2 = self.csp.getpagecode()
        self.csp.look_csp_data()  # 进入查看csp信息页面
        screenshoot.screen_shoot(self.driver, r'\csp', 'update_csp_type_success')
        value = self.csp.get_assert_text()

        try:
            self.assertIn(value, value2)
        except Exception:
            csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------csp类型变更审核失败--{value} is not in page ')
            raise
        else:
            csp_testlog.csp_log.info(
                f'Assertion Successed，case is  pass---------csp类型变更成功--{value} is  in page ')

    @unittest.skip('pass')
    def testcase07(self):
        """
        测试变更token且审核通过
        :return:
        """
        self.login.csp_login()
        self.login.wait(2)
        self.csp = CspPage(self.driver)
        self.csp.find_csp_data()  # 查询出数据
        self.csp.look_csp_data()  # 进入查看页面
        self.csp.update_csp('3')  # 更新token
        self.csp.intocheck()  # 进入审核内置表单
        self.csp.find_check_csp()  # 查询出待审核的数据
        self.csp.starting_check()  # 审核通过
        self.csp.intocheck(way='10')  #再次进入审核内置
        self.csp.find_check_csp(check_type='10')  #查询已审核的数据
        self.csp.look_checked_csp()  #点击查看已经审核的数据
        value = self.csp.look_update('1')  # 查看csptoken变更前后内容
        self.csp.wait(2)
        screenshoot.screen_shoot(self.driver, r'\csp', 'update_csp_token')
        try:
            self.assertTrue(value)
        except Exception:
            csp_testlog.csp_log.exception(
                f'Assertion Failed，case is not pass---------csp token变更失败--{value} 为假 ')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp token变更成功--{value} 为真 ')

    @unittest.skip('pass')
    def testcase08(self):
        """
        测试变更接入密匙且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        self.csp.find_csp_data()  # 查询出数据
        self.csp.look_csp_data()  # 进入查看页面
        self.csp.update_csp('4')  # 更新接入密匙
        self.csp.intocheck()  # 进入审核内置表单
        self.csp.find_check_csp()  # 查询出待审核的数据
        self.csp.starting_check()  # 审核通过
        self.csp.intocheck(way='10')  # 再次进入审核内置
        self.csp.find_check_csp(check_type='10')  # 查询已审核的数据
        self.csp.look_checked_csp()  # 点击查看已经审核的数据
        value = self.csp.look_update('2')  # 查看csp密匙变更前后内容
        self.csp.wait(2)
        screenshoot.screen_shoot(self.driver, r'\csp', 'update_csp_token')
        try:
            self.assertTrue(value)
        except Exception:
            csp_testlog.csp_log.exception(
                f'Assertion Failed，case is not pass---------csp token变更失败--{value} 为假 ')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp token变更成功--{value} 为真 ')

    @unittest.skip('pass')
    def testcase09(self):
        """
        测试上架csp且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        self.csp.find_csp_data()  #查询出数据
        self.csp.look_csp_data()  #进入查看页面
        self.csp.grounding_on()   #操作上架
        self.csp.grouding_check_form()   #进入上架审核内置表单
        self.csp.find_grounding_data()   #查询出待审核的上架申请
        self.csp.check_grounding()       #审核通过
        self.csp.look_gronding()         #查询已经上架的csp
        screenshoot.screen_shoot(self.driver, r'\csp', 'grouding_on')
        value = self.csp.get_assert_text()  #获取文本
        self.csp.wait(2)
        value2 = self.csp.getpagecode()
        try:
            self.assertIn(value,value2)
        except Exception:
            csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------{self.csp.add[1][-1]} 上架失败,{value} is not in page')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------{self.csp.add[1][-1]} 上架成功 {value}  in page ')

    @unittest.skip('pass')
    def testcase10(self):
        """
        测试下架csp
        :return:
        """
        self.csp = CspPage(self.driver)
        self.csp.find_csp_data()  # 查询出数据
        self.csp.look_csp_data()  # 进入查看页面
        self.csp.grounding_off()  #操作下架
        self.csp.look_gronding(result='未上架')  #查询已经下架的csp
        value2 = self.csp.getpagecode()
        screenshoot.screen_shoot(self.driver, r'\csp', 'grouding_off')
        value = self.csp.get_assert_text()
        try:
            self.assertIn(value,value2)
        except Exception:
            csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is not in page --{self.csp.add[1][-1]} 已经上架 ')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------{value} is in page --{self.csp.add[1][-1]} 未上架 ')

    @unittest.skip('pass')
    def testcase11(self):
        """
        测试已经下架的csp再次上架
        :return:
        """
        self.csp = CspPage(self.driver)
        self.csp.find_csp_data()  # 查询出数据
        self.csp.look_csp_data()  # 进入查看页面
        self.csp.grounding_on_again() #操作再次上架
        self.csp.grouding_check_form()  # 进入上架审核内置表单
        self.csp.find_grounding_data()  # 查询出待审核的上架申请
        self.csp.check_grounding()  # 审核通过
        self.csp.look_gronding()  # 查询已经上架的csp
        screenshoot.screen_shoot(self.driver, r'\csp', 'grouding_on_again')
        value = self.csp.get_assert_text()  # 获取文本
        self.csp.wait(2)
        value2 = self.csp.getpagecode()
        try:
            self.assertIn(value, value2)
        except Exception:
            csp_testlog.csp_log.exception(
                f'Assertion Failed，case is not pass---------{self.csp.add[1][-1]} 上架失败,{value} is not in page')
            raise
        else:
            csp_testlog.csp_log.info(
                f'Assertion Successed，case is  pass---------{self.csp.add[1][-1]} 上架成功 {value}  in page ')

    @unittest.skip('pass')
    def testcase12(self):
        """
        测试文件导入创建csp
        :return:
        """
        self.csp = CspPage(self.driver)
        cspname = self.csp.other_add()
        self.csp.find_check_csp()  # 查询出待审核的数据
        self.csp.starting_check()  # csp审核通过
        self.csp.find_csp_data(name=cspname)  # 管理节点查询出数据
        screenshoot.screen_shoot(self.driver, r'\csp', 'check_csp')
        value2 = self.csp.getpagecode()
        value = self.csp.get_assert_text(text=cspname)
        try:
            self.assertIn(value, value2)
        except Exception:
            csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------csp审核失败--{value} is not in page')
            raise
        else:
            csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp审核成功--{value} in page ')










if __name__=="__main__":
    unittest.main()
