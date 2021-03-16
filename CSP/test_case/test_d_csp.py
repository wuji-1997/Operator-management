from common.myunit import MYunit
from common.my_log import Log
import logging
import unittest
from Page.csp_page.csp_page import CspPage
from common import screenshoot
from common.writeexcel import Write_Excel
import time
from config import Conf
csp_testlog = Log(__name__,file=logging.INFO,cmd=logging.WARN)
writedata=Write_Excel(filepath=Conf.test_data+r'\test_csp_data.xlsx',number=5)

class Test_csp_manage(MYunit):


    #@unittest.skip('pass')
    def testcase01(self):
        """
        测试新建csp且审核不通过
        :return:
        """
        self.login.csp_login()
        self.login.wait(0.5)
        self.csp = CspPage(self.driver)
        newname =self.csp.random_number()
        value = self.csp.get_assert_text(text=newname)
        self.csp.new_csp(name=newname)  # 新增一个csp
        self.csp.intocheck(way=True)  # 进入csp审核节点
        self.csp.find_check_csp(cspname=newname)  # 查询待审核的csp数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.starting_check(result='20')  # 审核不通过
            self.csp.intocheck(way=False)
            self.csp.find_check_csp(cspname=newname, way='10', check_result='审核不通过')  # 查询已经审核通过的数据
            code2 = self.csp.getpagecode()
            screenshoot.screen_shoot(self.driver, r'\csp', '-01csp审核不通过创建失败')
            try:
                self.assertIn(value, code2)
            except Exception:
                csp_testlog.csp_log.exception(
                    f'Assertion Failed，case is not pass---------新建csp{self.csp.add_value[0]}失败--{value} is not in page')
                writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                csp_testlog.csp_log.info(
                    f'Assertion Successed，case is  passed---------新建csp{self.csp.add_value[0]}成功--{value} in page')
                writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            screenshoot.screen_shoot(self.driver, r'\csp', '-01新建csp失败')
            csp_testlog.csp_log.exception(f'查询的待审核数据{newname}---不存在')
            writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)

    #@unittest.skip('pass')
    def testcase02(self):
        """
        测试新建csp且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.new_csp()    #新增一个csp
        self.csp.intocheck(way=False)  #进入csp审核节点
        self.csp.find_check_csp()   #查询待审核的csp数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.wait(1)
            self.csp.starting_check()  #审核通过
            self.csp.intocheck(way=False)
            self.csp.find_check_csp(way='10')  #查询已经审核通过的数据
            screenshoot.screen_shoot(self.driver, r'\csp', '-02csp审核通过新增成功')
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
            screenshoot.screen_shoot(self.driver, r'\csp', '-02待审核数据不存在')
            writedata.update_data(2, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text= False
            self.assertTrue(text)
    #@unittest.skip('pass')
    def testcase03(self):
        """
        测试变更csp客户类型且审核不通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.updatecsp)
        if self.csp.assert_find(findname=self.csp.updatecsp,assert_text=value):
            self.csp.look_csp_data()  # 点击查看按钮
            self.csp.update_csp('1')  # 点击编辑按钮更新客户类型（变更为代理商）
            self.csp.intocheck(way=False)  # 进入审核内置表单
            self.csp.find_check_csp(cspname=self.csp.updatecsp,check_way='信息变更')  # 查询出待审核的数据
            code2 = self.csp.getpagecode()
            if value in code2:
                value2 = self.csp.get_assert_look_text(element_text=self.csp.update_value[0])
                self.csp.starting_check(result='10')  # 审核不通过
                self.csp.find_csp_data(name=self.csp.updatecsp)  # 查询出数据
                self.csp.look_csp_data()  # 进入查看csp信息页面
                screenshoot.screen_shoot(self.driver, r'\csp', '-03客户类型变更失败')
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
                screenshoot.screen_shoot(self.driver, '\csp', '-03修改客户类型失败')
                csp_testlog.csp_log.exception(f'未查询到待审核的数据---{self.csp.add_value[0]}')
                writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)
        else:
            screenshoot.screen_shoot(self.driver, r'\csp', '-03查询的csp不存在')
            csp_testlog.csp_log.exception(f'未查询到带变更的数据---{self.csp.updatecsp}')
            writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)

    #@unittest.skip('pass')
    def testcase04(self):
        """
        测试更新csp客户类型且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.updatecsp)
        if self.csp.assert_find(findname=self.csp.updatecsp,assert_text=value):
            self.csp.look_csp_data()  # 点击查看按钮
            self.csp.update_csp('1')  # 点击编辑按钮更新客户类型
            self.csp.intocheck(way=False)  # 进入审核内置表单
            self.csp.find_check_csp(cspname=self.csp.updatecsp,check_way='信息变更')  # 查询出待审核的数据
            code2 = self.csp.getpagecode()
            if value in code2:
                value2 = self.csp.get_assert_look_text(element_text=self.csp.update_value[0])
                self.csp.starting_check()  # 审核通过
                self.csp.find_csp_data(name=self.csp.updatecsp)  # 查询出数据
                self.csp.look_csp_data()  # 进入查看csp信息页面
                screenshoot.screen_shoot(self.driver, '\csp', '-04变更客户类型成功')
                code3 = self.csp.getpagecode()
                try:
                    self.assertIn(value2, code3)
                except Exception:
                    csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass---------csp客户类型变更审核失败--{value2} not in page ')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(f'测试案例通过------csp{self.csp.updatecsp}的客户类型变更为{self.csp.update_value[0]}')
                    writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                screenshoot.screen_shoot(self.driver, r'\csp', '-04待审核数据不存在')
                csp_testlog.csp_log.exception(f'未查询到待审核的数据---{self.csp.add_value[0]}')
                writedata.update_data(5,9,f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)
        else:
            screenshoot.screen_shoot(self.driver, r'\csp', '-04查询的csp不存在')
            csp_testlog.csp_log.exception(f'未查询到待变更的数据---{self.csp.add_value[0]}')
            writedata.update_data(5,9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)

    #@unittest.skip('pass')
    def testcase05(self):
        """
        测试变更csp token且审核通过
        :return:
        """

        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.updatecsp)
        if self.csp.assert_find(findname=self.csp.updatecsp, assert_text=value):
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.update_csp('3')  # 更新token
            self.csp.intocheck(way=False)  # 进入审核内置表单无需身份验证
            self.csp.find_check_csp(cspname=self.csp.updatecsp,check_way='信息变更')  # 查询出待审核的数据
            code2 =self.csp.getpagecode()
            if value in code2:
                self.csp.starting_check()  # 审核通过
                self.csp.wait(2)
                self.csp.intocheck(way=False)   #进入审核内置表单
                self.csp.click_element(self.csp.check[1][11], self.csp.check[2][11])  # 点击已审核
                #self.csp.find_check_csp(cspname=self.csp.updatecsp,way='10')  #查询已审核的数据
                self.csp.look_checked_csp()  #点击查看已经审核的数据
                value2 = self.csp.look_update('1')  # 查看csptoken变更前后内容
                self.csp.wait(2)
                screenshoot.screen_shoot(self.driver, r'\csp', '-05变更csp--token成功')
                try:
                    self.assertTrue(value2)
                except Exception:
                    csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass---------csp token变更失败--判断条件为{value2} ')
                    writedata.update_data(8, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp token变更成功--判断条件为{value2}')
                    writedata.update_data(8, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                screenshoot.screen_shoot(self.driver, r'\csp', '-05待审核数据不存在')
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                writedata.update_data(8, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)


        else:
            screenshoot.screen_shoot(self.driver, r'\csp', '-05查询的csp不存在')
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(8, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)

    #@unittest.skip('pass')
    def testcase06(self):
        """
        测试变更csp接入密匙且审核通过
        :return:
        """

        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.updatecsp)
        if self.csp.assert_find(findname=self.csp.updatecsp, assert_text=value):
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.update_csp('4')  # 更新密匙
            self.csp.wait(2)
            self.csp.intocheck(way=False)  # 进入审核内置表单无需身份验证
            self.csp.find_check_csp(cspname=self.csp.updatecsp, check_way='信息变更')  # 查询出待审核的数据
            code2 = self.csp.getpagecode()
            if value in code2:
                self.csp.wait(2)
                self.csp.starting_check()  # 审核通过
                self.csp.wait(2)
                self.csp.intocheck(way=False)  # 进入审核内置表单
                self.csp.click_element(self.csp.check[1][11], self.csp.check[2][11])  # 点击已审核
                #self.csp.find_check_csp(cspname=self.csp.updatecsp,way='10')  # 查询已审核的数据
                self.csp.look_checked_csp()  # 点击查看已经审核的数据
                value2 = self.csp.look_update('2')  # 查看csptoken变更前后内容
                self.csp.wait(2)
                screenshoot.screen_shoot(self.driver, r'\csp', '-06变更csp--接入密匙成功')
                try:
                    self.assertTrue(value2)
                except Exception:
                    csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass---------csp token变更失败--判断条件为{value2} ')
                    writedata.update_data(9, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                    raise
                else:
                    csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------csp token变更成功--判断条件为{value2}')
                    writedata.update_data(9, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
            else:
                screenshoot.screen_shoot(self.driver, r'\csp', '-06待审核csp不存在')
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.updatecsp}不存在')
                text = False
                self.assertTrue(text)
                writedata.update_data(9, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


        else:
            screenshoot.screen_shoot(self.driver, r'\csp', '-06查询的csp不存在')
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            text = False
            self.assertTrue(text)
            writedata.update_data(9, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


    #@unittest.skip('pass')
    def testcase07(self):
        """
        测试更新csp类型且审核不通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.updatecsp)
        if self.csp.assert_find(findname=self.csp.updatecsp,assert_text=value):
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.update_csp('2')  # 更新csp类型
            self.csp.F5()
            self.csp.intocheck(way=False)  # 进入审核内置表单
            self.csp.find_check_csp(cspname=self.csp.updatecsp,check_way='信息变更')  # 查询出待审核的数据
            code2 = self.csp.getpagecode()
            if value in code2:
                self.csp.starting_check(result='10')  # 审核不通过
                self.csp.find_csp_data(name=self.csp.updatecsp,csp_type=self.csp.update_value[1])  # 查询出数据
                code2 = self.csp.getpagecode()
                screenshoot.screen_shoot(self.driver, r'\csp', '-06变更csp类型失败')

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
                screenshoot.screen_shoot(self.driver, r'\csp', '-06待变更数据不存在')
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                text = False
                self.assertTrue(text)
                writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


        else:
            screenshoot.screen_shoot(self.driver, r'\csp', '-06查询的csp不存在')
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            text = False
            self.assertTrue(text)
            writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


    #@unittest.skip('pass')
    def testcase08(self):
        """
        测试更新csp类型且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.updatecsp)
        if self.csp.assert_find(findname=self.csp.updatecsp, assert_text=value):
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.update_csp('2')  # 更新csp类型
            self.csp.intocheck(way=False)  # 进入审核内置表单
            self.csp.find_check_csp(cspname=self.csp.updatecsp,check_way='信息变更')  # 查询出待审核的数据
            code2 =self.csp.getpagecode()
            if value in code2:
                self.csp.starting_check()  # 审核通过
                self.csp.find_csp_data(name=self.csp.updatecsp,csp_type=self.csp.update_value[1])  # 查询出数据
                code3 = self.csp.getpagecode()
                screenshoot.screen_shoot(self.driver, r'\csp', '-08变更csp类型成功')

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
                screenshoot.screen_shoot(self.driver, r'\csp', '-08csp类型变更待审核数据不存在')
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                text = False
                self.assertTrue(text)
                writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


        else:
            screenshoot.screen_shoot(self.driver, r'\csp', '-07查询的csp不存在')
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            text = False
            self.assertTrue(text)
            writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


    #@unittest.skip('pass')
    def testcase09(self):
        """
        测试上架csp且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data()  #查询出数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  #进入查看页面
            self.csp.grounding_on()   #操作上架
            self.csp.grouding_check_form(grounding_way=False)   #进入上架审核内置表单
            self.csp.find_grounding_data()   #查询出待审核的上架申请
            code2 =self.csp.getpagecode()
            if value in code2:
                self.csp.check_grounding()       #审核通过
                self.csp.look_gronding(status=True)         #查询已经上架的csp
                screenshoot.screen_shoot(self.driver, r'\csp', '-09csp上架成功')
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
                screenshoot.screen_shoot(self.driver,r'\csp','-09未查询到待审核的上架申请')
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                text = False
                self.assertTrue(text)
                writedata.update_data(10, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


        else:
            screenshoot.screen_shoot(self.driver,r'\csp','-09未查询到待上架的csp')
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            text = False
            self.assertTrue(text)
            writedata.update_data(10, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


    #@unittest.skip('pass')
    def testcase10(self):
        """
        测试下架csp
        :return:
        """

        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        value2 = '上架状态：已下架'
        self.csp.find_csp_data()  # 查询出数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.grounding_off()  #操作下架
            self.csp.wait(1)
            self.csp.look_gronding(status=False)  #查询已经下架的csp
            self.csp.look_csp_data()
            value1 = self.csp.getpagecode()
            screenshoot.screen_shoot(self.driver, r'\csp', '-10csp下架成功')
            try:
                self.assertIn(value2,value1)
            except Exception:
                csp_testlog.csp_log.exception(f'Assertion Failed，case is not pass---------{value2} not in page --{self.csp.add_value[0]} 已经上架 ')
                writedata.update_data(11, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise
            else:
                csp_testlog.csp_log.info(f'Assertion Successed，case is  pass---------{value2} in page --{self.csp.add_value[0]} 未上架 ')
                writedata.update_data(11, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            screenshoot.screen_shoot(self.driver,'\csp','-10未查询到待下架的csp')
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            text = False
            self.assertTrue(text)
            writedata.update_data(11, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")


    #@unittest.skip('pass')
    def testcase11(self):
        """
        测试已经下架的csp再次上架
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text()
        self.csp.find_csp_data()  # 查询出数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.grounding_on_again() #操作再次上架
            self.csp.wait(1)
            self.csp.grouding_check_form(grounding_way=False)  # 进入上架审核内置表单
            self.csp.find_grounding_data()  # 查询出待审核的上架申请
            code2 = self.csp.getpagecode()
            if value in code2:
                self.csp.check_grounding()  # 审核通过
                self.csp.look_gronding(status=True,result='已上架')  # 查询已经上架的csp
                screenshoot.screen_shoot(self.driver, r'\csp', '-11csp再次上架成功')
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
                screenshoot.screen_shoot(self.driver, r'\csp', '-11未查询到待审核的再次上架申请')
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
                writedata.update_data(12, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)

        else:
            screenshoot.screen_shoot(self.driver,r'csp','-11未查询到再次上架的csp')
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(12, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)



    #@unittest.skip('pass')
    def testcase12(self):
        """
        测试文件导入创建csp且审核不通过
        :return:
        """
        self.csp = CspPage(self.driver)
        newname=self.csp.random_number()
        value = self.csp.get_assert_text(text=newname)
        self.csp.other_add(add_name=newname)
        self.csp.intocheck(way=False)  #进入审核内置表单
        self.csp.find_check_csp(cspname=newname)  # 查询出待审核的数据
        code = self.csp.getpagecode()
        if value in code:
            self.csp.starting_check(result='10')  # 审核通过
            self.csp.intocheck(way=False)
            self.csp.find_check_csp(cspname=newname,way='10',check_result='审核不通过')  # 查询已经审核通过的数据
            screenshoot.screen_shoot(self.driver, r'\csp', '-12文件导入新建csp不通过')
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
            screenshoot.screen_shoot(self.driver, '\csp', '-12待审核的csp查询不到')
            csp_testlog.csp_log.exception(f'查询的待审核数据--{newname}不存在')
            writedata.update_data(14, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)

    #@unittest.skip('pass')
    def testcase13(self):
        """
        测试文件导入创建csp且审核通过
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.other_add_csp)
        self.csp.other_add()
        self.csp.intocheck(way=False)  # 进入审核内置表单
        self.csp.find_check_csp(cspname=self.csp.other_add_csp)  # 查询出待审核的数据
        code = self.csp.getpagecode()
        if value in code:
           self.csp.starting_check()  # 审核通过
           self.csp.intocheck(way=False)
           self.csp.find_check_csp(cspname=self.csp.other_add_csp, way='10')  # 查询已经审核通过的数据
           screenshoot.screen_shoot(self.driver, r'\csp', '-11文件导入新建csp成功')
           code2 = self.csp.getpagecode()
           try:
               self.assertIn(value, code2)
           except Exception:
               csp_testlog.csp_log.exception(
                        f'Assertion Failed，case is not pass-----导入文件新建csp失败--{value} is not in page')
               writedata.update_data(13, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
               raise
           else:
                csp_testlog.csp_log.info(f'Assertion Successed，case is  pass-------导入文件新建csp成功--{value} in page ')
                writedata.update_data(13, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            screenshoot.screen_shoot(self.driver, '\csp', '-11待审核的csp查询不到')
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.add_value[0]}不存在')
            writedata.update_data(13, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)


    #@unittest.skip('pass')
    def testcase14refresh(self):
        """
        测试数据复原
        :return:
        """
        self.csp = CspPage(self.driver)
        value = self.csp.get_assert_text(text=self.csp.updatecsp)
        if self.csp.assert_find(findname=self.csp.updatecsp,assert_text=value,findtype=self.csp.update_value[1]):
            self.csp.look_csp_data()  # 进入查看页面
            self.csp.refresh()
            self.csp.F5()
            self.csp.intocheck(way=False)  # 进入审核内置表单
            self.csp.find_check_csp(cspname=self.csp.updatecsp,check_csp_type=self.csp.update_value[1],check_way='信息变更')  # 查询出待审核的数据
            code2 = self.csp.getpagecode()
            if value in code2:
                self.csp.starting_check()  # 审核通过
                self.csp.find_csp_data(name=self.csp.updatecsp,csp_type=self.csp.add_value[2])  # 查询出数据
                code3 = self.csp.getpagecode()
                screenshoot.screen_shoot(self.driver, r'\csp', '-14变更csp与客户类型成功')
                try:
                    self.assertIn(value, code3)
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
                screenshoot.screen_shoot(self.driver, r'\csp', '-14查询的待审核csp不存在')
                csp_testlog.csp_log.exception(f'查询的数据--{self.csp.updatecsp}不存在')
                writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                text = False
                self.assertTrue(text)

        else:
            screenshoot.screen_shoot(self.driver, r'\csp', '-14查询的csp不存在')
            csp_testlog.csp_log.exception(f'查询的数据--{self.csp.updatecsp}不存在')
            writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            text = False
            self.assertTrue(text)



if __name__=="__main__":
    unittest.main()
