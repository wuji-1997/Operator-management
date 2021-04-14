from common.myunit import MYunit
from common.my_log import Log
import logging
import unittest
from Page.csp_page.system_management_page import SyStem_Management_Page
from common import screenshoot
from common.writeexcel import Write_Excel
from config import Conf
import time
writedata=Write_Excel(filepath=Conf.test_data+r'\test_system.xlsx',number=4)
test_system_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_csp_system(MYunit):

    @unittest.skip('pass')
    def testcase34(self):
        """
        测试新增一个账号且可登录系统
        :return:
        """
        self.login.csp_login()
        self.login.wait(2)
        self.system = SyStem_Management_Page(self.driver)
        self.system.add_user()      #新增一个账号
        self.login.csplogin(newname=self.system.add_value[0], newpws=self.system.add_value[9])
        self.login.wait(2)
        screenshoot.screen_shoot(self.driver,r'\system','-01新建账号登录成功')
        value2 = self.login.get_url()
        try:
            self.assertEqual(self.login.url, value2)
        except Exception:
            writedata.update_data(2, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
            test_system_log.csp_log.exception(f'Assertion Failed，case is not passed------{self.login.url}!={value2} ')
            raise
        else:
            test_system_log.csp_log.info(f'Assertion Success，case is  passed------{self.login.url}={value2}')
            writedata.update_data(2, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")

    @unittest.skip('pass')
    def testcase35(self):
        """
        测试变更账号再次登录可成功
        :return:
        """
        self.system = SyStem_Management_Page(self.driver)
        value = self.system.assert_text(text=self.system.add_value[11])
        self.system.intouser()    #进入内置表单
        self.system.find_user(username=self.system.add_value[11],realname=self.system.add_value[13])   #查询账号
        code=self.system.getpagecode()
        if value in code:
            self.system.update_user(way=True)  #更新用户名
            self.login.csplogin(newname=self.system.add_value[10], newpws=self.system.add_value[12])
            self.login.wait(2)
            screenshoot.screen_shoot(self.driver, r'\system', '-02变更账号信息登录成功')
            value2 = self.login.get_url()
            try:
                self.assertEqual(self.login.url, value2)
            except Exception:
                writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                test_system_log.csp_log.exception(
                    f'Assertion Failed，case is not passed------{self.login.url}!={value2} ')
                raise
            else:
                test_system_log.csp_log.info(f'Assertion Success，case is  passed------{self.login.url}={value2}')
                writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text=False
            try:
                self.assertTrue(text)
            except Exception:
                test_system_log.csp_log.exception(f'未查询待变更的账号数据----{self.system.add_value[0]}--------请重新调试案例')
                writedata.update_data(3, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise

    @unittest.skip('pass')
    def testcase36(self):
        """
        测试变更密码再次登录可成功
        :return:
        """
        self.system = SyStem_Management_Page(self.driver)
        value = self.system.assert_text(text=self.system.add_value[10])
        pws=self.system.add_value[14]
        self.system.intouser()  # 进入内置表单
        self.system.find_user(username=self.system.add_value[10], realname=self.system.add_value[13])  # 查询账号
        code=self.system.getpagecode()
        if value in code:
            self.system.update_user(way=False,updatepws=pws)  #更新密码
            self.login.csplogin(newname=self.system.add_value[10], newpws=pws)
            self.login.wait(2)
            screenshoot.screen_shoot(self.driver, r'\system', '-02变更账号密码登录成功')
            value2 = self.login.get_url()
            try:
                self.assertEqual(self.login.url, value2)
            except Exception:
                writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                test_system_log.csp_log.exception(
                    f'Assertion Failed，case is not passed------{self.login.url}!={value2} ')
                raise
            else:
                test_system_log.csp_log.info(f'Assertion Success，case is  passed------{self.login.url}={value2}')
                writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text=False
            try:
                self.assertTrue(text)
            except Exception:
                test_system_log.csp_log.exception(f'未查询待变更的账号数据----{self.system.add_value[0]}--------请重新调试案例')
                writedata.update_data(4, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise



    @unittest.skip('pass')
    def testcase37(self):
        """
        测试停用账号
        :return:
        """
        self.system = SyStem_Management_Page(self.driver)
        value=self.system.assert_text(text=self.system.add_value[10])
        self.system.intouser()
        self.system.find_user(username=self.system.add_value[10],realname=self.system.add_value[13])  # 查询账号
        code=self.system.getpagecode()
        if value in code:
            self.system.stop_user()  #停用账号
            self.login.csplogin(newname=self.system.add_value[10], newpws=self.system.add_value[14])
            self.login.wait(2)
            screenshoot.screen_shoot(self.driver, r'\system', '-03账户已被冻结登录失败')
            value2 = self.login.get_url()
            try:
                self.assertNotEqual(self.login.url, value2)
            except Exception:
                writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                test_system_log.csp_log.exception(
                    f'Assertion Failed，case is not passed------{self.login.url}={value2} ')
                raise
            else:
                test_system_log.csp_log.info(f'Assertion Success，case is  passed------{self.login.url}!={value2}')
                writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text=False
            try:
                self.assertTrue(text)
            except Exception:
                test_system_log.csp_log.exception(f'未查询待停用的账号数据----{self.system.add_value[10]}--------请重新调试案例')
                writedata.update_data(5, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise

    @unittest.skip('pass')
    def testcase38(self):
        """
        测试重新启用账号
        :return:
        """
        self.system = SyStem_Management_Page(self.driver)
        value = self.system.assert_text(text=self.system.add_value[10])
        self.system.wait(40)
        self.system.F5()
        self.login.other_login()
        self.system.intouser()
        self.system.find_user(username=self.system.add_value[10], realname=self.system.add_value[13],userstatus='禁用')  # 查询账号
        code=self.system.getpagecode()
        if value in code:
            self.system.start_user()
            self.login.csplogin(newname=self.system.add_value[10], newpws=self.system.add_value[14])
            self.system.wait(3)
            value2 = self.login.get_url()
            self.system.wait(4)
            screenshoot.screen_shoot(self.driver, r'\system', '-05重新启用账号登录成功')
            self.system.wait(1)
            self.system.intouser()
            self.system.find_user(username=self.system.add_value[10], realname=self.system.add_value[13])  # 查询账号
            self.system.refresh()
            try:
                self.assertEqual(self.login.url, value2)

            except Exception:
                writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                test_system_log.csp_log.exception(
                    f'Assertion Failed，case is not passed------{self.login.url}！={value2} ')
                raise
            else:
                test_system_log.csp_log.info(f'Assertion Success，case is  passed------{self.login.url}={value2}')
                writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_system_log.csp_log.exception(f'未查询待启用的账号数据----{self.system.add_value[10]}--------请重新调试案例')
                writedata.update_data(6, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise


    @unittest.skip('pass')
    def testcase39(self):
        """
        测试删除账号
        :return:
        """
        self.system = SyStem_Management_Page(self.driver)
        value = self.system.assert_text(text=self.system.add_value[0])
        self.system.intouser()
        self.system.find_user()  # 查询账号
        code = self.system.getpagecode()
        if value in code:
            self.system.detele_user()
            self.login.csplogin(newname=self.system.add_value[0], newpws=self.system.add_value[9])
            self.login.wait(2)
            screenshoot.screen_shoot(self.driver, r'\system', '-06删除账号登录失败')
            value2 = self.login.get_url()
            try:
                self.assertNotEqual(self.login.url, value2)
            except Exception:
                writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                test_system_log.csp_log.exception(
                    f'Assertion Failed，case is not passed------{self.login.url}={value2} ')
                raise
            else:
                test_system_log.csp_log.info(f'Assertion Success，case is  passed------{self.login.url}!={value2}')
                writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行通过")
        else:
            text = False
            try:
                self.assertTrue(text)
            except Exception:
                test_system_log.csp_log.exception(f'未查询待删除的账号数据----{self.system.add_value[10]}--------请重新调试案例')
                writedata.update_data(7, 9, f"{time.strftime('%Y-%m-%d %H:%M:%S')}案例执行不通过")
                raise






if __name__=="__main__":
    unittest.main()









