from common.myunit import MYunit
from common.my_log import Log
import logging
import unittest
from Page.csp_page import CspPage
from common import screenshoot
from common.writeexcel import Write_Excel
import time
from config import Conf
csp_testlog = Log(__name__,file=logging.INFO,cmd=logging.INFO)
writedata=Write_Excel(filepath=Conf.test_data+r'\test_csp_data.xlsx',number=5)

class Test_csp(MYunit):


    def testcase01(self):
        """
        测试新增CSP且审核通过
        :return:
        """
        self.login.csp_login()
        self.login.wait(2)
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.new_csp()    #新增一个csp
        self.csp.intocheck()  #进入csp审核节点
        self.csp.find_check_csp()   #查询待审核的csp数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.starting_check()  #审核通过
            self.csp.intocheck(way='10')
            self.csp.find_check_csp(way='10')  #查询已经审核通过的数据
            code2 = self.csp.getpagecode()
            try:
                self.assertIn(value,code2)
            except Exception:
                csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------新建csp{self.csp.add_value[0]}失败--{value} is not in page')
                writedata.update_data(2,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                csp_testlog.csp_log.info(f'Assertion Successed，case is  passed---------新建csp{self.csp.add_value[0]}成功--{value} in page')
                writedata.update_data(2,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            writedata.update_data(2, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text= False
            self.assertTrue(text)


    def testcase02(self):
        """
        测试审核创建csp的流程且审核不通过
        :return:
        """

        self.csp = CspPage(self.driver)
        newname = self.csp.add_value[0] + '2'
        value = self.csp.get_assert_text(text=newname)
        self.csp.new_csp(name=newname)  # 新增一个csp
        self.csp.intocheck(way=None)  # 进入csp审核节点
        self.csp.find_check_csp()  # 查询待审核的csp数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.starting_check(result='2')  # 审核不通过
            self.csp.intocheck(way='10')
            self.csp.find_check_csp(way='10',check_result='审核不通过')  # 查询已经审核通过的数据
            code2 = self.csp.getpagecode()

            try:
                self.assertIn(value, code2)
            except Exception:
                csp_testlog.csp_log.exception(
                    f'Assertion Failed，case is not pass---------新建csp{self.csp.add_value[0]}失败--{value} is not in page')
                writedata.update_data(3,9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                csp_testlog.csp_log.info(
                    f'Assertion Successed，case is  passed---------新建csp{self.csp.add_value[0]}成功--{value} in page')
                writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            csp_testlog.csp_log.exception(f'查询的待审核数据{newname}---不存在')
            writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)


    def testcase03(self):
        """
        测试客户变更审核不通过
        :return:
        """

        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data()  # 进入管理页面查询出审核通过的csp数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  # 点击查看按钮
            self.csp.update_csp('1')  # 点击编辑按钮更新客户类型
            self.csp.intocheck(way='5')  # 进入审核内置表单
            self.csp.find_check_csp(check_way='信息变更')  # 查询出待审核的数据
            code2 = self.csp.getpagecode()
            if value in code2:
                value2 = self.csp.get_assert_look_text(element_text=self.csp.update_value[0])
                self.csp.wait(2)
                self.csp.starting_check(result='10')  # 审核不通过
                self.csp.find_csp_data()  # 查询出数据
                self.csp.look_csp_data()  # 进入查看csp信息页面
                screenshoot.screen_shoot(self.driver, r'\csp', '变更csp客户类型失败')
                code3 = self.csp.getpagecode()
                try:
                    self.assertNotIn(value2,code3)
                except Exception:
                    csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass---------csp客户类型变更审核失败--{value2}  in page ')
                    writedata.update_data(4,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(f'Assertion Successed，case is  pass-----csp客户类型变更审核不通过成功--{value2} is not in page')
                    writedata.update_data(4,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                csp_testlog.csp_log.exception(f'未查询到待审核的数据---{self.csp.add_value[0]}')
                writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)
        else:
            csp_testlog.csp_log.exception(f'未查询到带变更的数据---{self.csp.add_value[0]}')
            writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)


    def testcase04(self):
        """
        测试更新csp客户类型且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data()  # 进入管理页面查询出审核通过的csp数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  # 点击查看按钮
            self.csp.update_csp('1')  # 点击编辑按钮更新客户类型
            self.csp.intocheck(way='10')  # 进入审核内置表单
            self.csp.find_check_csp(check_way='信息变更')  # 查询出待审核的数据
            code2 = self.csp.getpagecode()
            if value in code2:
                self.csp.starting_check()  # 审核通过
                self.csp.find_csp_data()  # 查询出数据
                self.csp.look_csp_data()  # 进入查看csp信息页面
                screenshoot.screen_shoot(self.driver, r'\csp', '变更csp客户类型成功')
                code3 = self.csp.getpagecode()
                value2 = self.csp.get_assert_look_text(element_text=self.csp.update_value[0])
                try:
                    self.assertIn(value2, code3)
                except Exception:
                    csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass---------csp客户类型变更审核失败--{value2}  not in page ')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(
                        f'Assertion Successed，case is  pass-----csp客户类型变更审核不通过成功--{value2} is  in page')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                text = False
                self.assertTrue(text)
                csp_testlog.csp_log.exception(f'未查询到待审核的数据---{self.csp.add_value[0]}')
                writedata.update_data(5,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
        else:
            text = False
            self.assertTrue(text)
            csp_testlog.csp_log.exception(f'未查询到待变更的数据---{self.csp.add_value[0]}')
            writedata.update_data(5,9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


    def testcase05(self):
        """
        测试更新csp类型且审核不通过
        :return:
        """

        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data()  # 查询出数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.update_csp('2')  # 更新csp类型
            self.csp.intocheck(way='10')  # 进入审核内置表单
            self.csp.find_check_csp(check_way='信息变更')  # 查询出待审核的数据
            code2 = self.csp.getpagecode()
            if value in code2:
                self.csp.starting_check(result='10')  # 审核不通过
                self.csp.find_csp_data(csp_type=self.csp.update_value[1])  # 查询出数据
                code2 = self.csp.getpagecode()
                screenshoot.screen_shoot(self.driver, r'\csp', '变更csp类型失败')

                try:
                    self.assertNotIn(value,code2)
                except Exception:
                    csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------csp类型变更审核失败--{value}  in page ')
                    writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp类型变更审核不通过成功--{value} is not in page ')
                    writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)

        else:
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)


    def testcase06(self):
        """
        测试更新csp类型且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data()  # 查询出数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.update_csp('2')  # 更新csp类型
            self.csp.intocheck(way='10')  # 进入审核内置表单
            self.csp.find_check_csp(check_way='信息变更')  # 查询出待审核的数据
            code2 =self.csp.getpagecode()
            if value in code2:
                self.csp.starting_check()  # 审核通过
                self.csp.find_csp_data(csp_type=self.csp.update_value[1])  # 查询出数据
                code3 = self.csp.getpagecode()
                screenshoot.screen_shoot(self.driver, r'\csp', '变更csp类型失败')

                try:
                    self.assertIn(value,code3)
                except Exception:
                    csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass---------csp类型变更审核失败--{value}  not in page ')
                    writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(
                        f'Assertion Successed，case is  pass---------csp类型变更审核通过成功--{value}  in page ')
                    writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)

        else:
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)


    def testcase07(self):
        """
        测试变更token且审核通过
        :return:
        """

        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data(csp_type=self.csp.update_value[1])  # 查询出数据
        code = self.csp.getpagecode()
        if value in  code:
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.update_csp('3')  # 更新token
            self.csp.intocheck(way='10')  # 进入审核内置表单无需身份验证
            self.csp.find_check_csp(check_way='信息变更',check_csp_type=self.csp.update_value[1])  # 查询出待审核的数据
            code2 =self.csp.getpagecode()
            if value in code2:
                self.csp.starting_check()  # 审核通过
                self.csp.wait(2)
                self.csp.find_check_csp(way='10',check_csp_type=self.csp.update_value[1])  #查询已审核的数据
                self.csp.look_checked_csp()  #点击查看已经审核的数据
                value2 = self.csp.look_update('1')  # 查看csptoken变更前后内容
                self.csp.wait(2)
                screenshoot.screen_shoot(self.driver, r'\csp', '变更csp--token成功')
                try:
                    self.assertTrue(value2)
                except Exception:
                    csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass---------csp token变更失败--{value} 为假 ')
                    writedata.update_data(8, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp token变更成功--{value} 为真 ')
                    writedata.update_data(8, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                writedata.update_data(8, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)


        else:
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(8, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)


    def testcase08(self):
        """
        测试变更接入密匙且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data(csp_type=self.csp.update_value[1])  # 查询出数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.update_csp('4')  # 更新token
            self.csp.intocheck(way='10')  # 进入审核内置表单无需身份验证
            self.csp.find_check_csp(check_way='信息变更',check_csp_type=self.csp.update_value[1])  # 查询出待审核的数据
            code2 =self.csp.getpagecode()
            if value in code2:
                self.csp.starting_check()  # 审核通过
                self.csp.wait(2)
                self.csp.find_check_csp(check_type='10', check_csp_type=self.csp.update_value[1])  # 查询已审核的数据
                self.csp.look_checked_csp()  # 点击查看已经审核的数据
                value2 = self.csp.look_update('2')  # 查看csptoken变更前后内容
                self.csp.wait(2)
                screenshoot.screen_shoot(self.driver, r'\csp', '变更csp--token成功')
                try:
                    self.assertTrue(value2)
                except Exception:
                    csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass---------csp token变更失败--{value2} 为假 ')
                    writedata.update_data(9,9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp token变更成功--{value2} 为真 ')
                    writedata.update_data(9, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                writedata.update_data(9, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)

        else:
            text = False
            self.assertTrue(text)
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(9, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


    def testcase09(self):
        """
        测试上架csp且审核通过
        :return:
        """

        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data(csp_type=self.csp.update_value[1])  #查询出数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  #进入查看页面
            self.csp.grounding_on()   #操作上架
            self.csp.grouding_check_form()   #进入上架审核内置表单
            self.csp.find_grounding_data(gronding_csp_type=self.csp.update_value[1])   #查询出待审核的上架申请
            code2 =self.csp.getpagecode()
            if value in code2:
                self.csp.check_grounding()       #审核通过
                self.csp.look_gronding()         #查询已经上架的csp
                screenshoot.screen_shoot(self.driver, r'\csp', 'csp上架成功')
                value = self.csp.get_assert_text()  #获取文本
                self.csp.wait(2)
                value2 = self.csp.getpagecode()
                try:
                    self.assertIn(value,value2)
                except Exception:
                    csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------{self.csp.add_value[0]} 上架失败,{value} is not in page')
                    writedata.update_data(10, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------{self.csp.add_value[0]} 上架成功 {value}  in page ')

                    writedata.update_data(10, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                writedata.update_data(10, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)

        else:
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(10, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)


    def testcase10(self):
        """
        测试下架csp
        :return:
        """

        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data(csp_type=self.csp.update_value[1])  # 查询出数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.grounding_off()  #操作下架
            self.csp.look_gronding(result='未上架')  #查询已经下架的csp
            code2 = self.csp.getpagecode()
            screenshoot.screen_shoot(self.driver, r'\csp', 'csp下架')
            try:
                self.assertIn(value,code2)
            except Exception:
                csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------{value} is not in page --{self.csp.add_value[0]} 已经上架 ')
                writedata.update_data(11, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------{value} is  in page --{self.csp.add_value[0]} 未上架 ')
                writedata.update_data(11, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(11, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)



    def testcase11(self):
        """
        测试已经下架的csp再次上架
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data(csp_type=self.csp.update_value[1])  # 查询出数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.grounding_on_again() #操作再次上架
            self.csp.grouding_check_form(grounding_way='10')  # 进入上架审核内置表单
            self.csp.find_grounding_data(gronding_csp_type=self.csp.update_value[1])  # 查询出待审核的上架申请
            code2 = self.csp.getpagecode()
            if value in code2:
                self.csp.check_grounding()  # 审核通过
                self.csp.look_gronding(result='已上架')  # 查询已经上架的csp
                screenshoot.screen_shoot(self.driver, r'\csp', 'csp再次上架成功')
                value = self.csp.get_assert_text()  # 获取文本
                self.csp.wait(2)
                value2 = self.csp.getpagecode()
                try:
                    self.assertIn(value, value2)
                except Exception:
                    csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass---------{self.csp.add[1][-1]} 上架失败,{value} is not in page')
                    writedata.update_data(12, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(
                        f'Assertion Successed，case is  pass---------{self.csp.add[1][-1]} 上架成功 {value}  in page ')
                    writedata.update_data(12, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                writedata.update_data(12, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)

        else:
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(12, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)



    def testcase12(self):
        """
        测试文件导入创建csp且审核通过
        :return:
        """

        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.other_add_csp)
        self.csp.other_add()
        self.csp.intocheck(way='10')  #进入审核内置表单
        self.csp.find_check_csp(cspname=self.csp.other_add_csp)  # 查询出待审核的数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.starting_check()  # 审核通过
            self.csp.intocheck(way='10')
            self.csp.find_check_csp(cspname=self.csp.other_add_csp,way='10')  # 查询已经审核通过的数据
            screenshoot.screen_shoot(self.driver, r'\csp', '文件导入新建csp')
            code2 = self.csp.getpagecode()
            try:
                self.assertIn(value,code2)
            except Exception:
                csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass-----导入文件新建csp失败--{value} is not in page')
                writedata.update_data(13, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                csp_testlog.csp_log.info(f'Assertion Successed，case is  pass-------导入文件新建csp成功--{value} in page ')
                writedata.update_data(13, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(13, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)


    def testcase13(self):
        """
        测试文件导入创建csp且审核不通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.add_value[24])
        self.csp.other_add(add_name=self.csp.add_value[24])
        self.csp.intocheck(way='10')  #进入审核内置表单
        self.csp.find_check_csp(cspname=self.csp.add_value[24])  # 查询出待审核的数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.starting_check(result='10')  # 审核通过
            self.csp.intocheck(way='10')
            self.csp.find_check_csp(cspname=self.csp.add_value[24],way='10',check_result='审核不通过')  # 查询已经审核通过的数据
            screenshoot.screen_shoot(self.driver, r'\csp', '文件导入新建csp')
            code2 = self.csp.getpagecode()
            try:
                self.assertIn(value,code2)
            except Exception:
                csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass-----导入文件新建csp失败--{value} is  in page')
                writedata.update_data(14, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                csp_testlog.csp_log.info(f'Assertion Successed，case is  pass-------导入文件新建csp成功--{value} not in page ')
                writedata.update_data(14, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(14, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)



if __name__=="__main__":
    unittest.main()
