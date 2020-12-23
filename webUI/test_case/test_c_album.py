from webUI.common.my_log import Log
from webUI.common.my_unit import MYunit
import logging
import unittest
from webUI.common import screenshoot

from webUI.Page.album_page import AlbumPage


testalbum_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

class TestAlbum(MYunit):


    def test_a_newalbum(self):
        """
        测试新建相册
        :return:
        """
        self.login.login()
        self.login.wait(5)
        self.album = AlbumPage(self.driver)

        self.album.new_album()
        self.album.wait(5)
        screenshoot.screen_shoot(self.driver,"new_album")
        value = self.album.albumname[-1]
        value2 = self.album.getpagecode()
        try:

            self.assertIn(value, value2)

        except Exception:
            testalbum_log.action_log.exception(f'断言失败，案例不通过---------{value}不在当前页面')
            raise

        else:
            testalbum_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value}在当前页面')


    def test_b_updatealbum(self):
        """
        测试更新相册
        :return:
        """

        self.album = AlbumPage(self.driver)
        self.album.update_album()
        self.album.wait(5)

        screenshoot.screen_shoot(self.driver,"update_album")

        value = self.album.newalbumname
        value2=self.album.getpagecode()
        try:

            self.assertIn(value, value2)

        except Exception:
            testalbum_log.action_log.exception(f'断言失败，案例不通过---------{value}不在当前页面')
            raise

        else:
            testalbum_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value}在当前页面')

    def test_c_deletealbum(self):
        """
        测试删除相册
        :return:
        """

        self.album = AlbumPage(self.driver)
        self.album.delete_album()
        self.album.wait(5)

        screenshoot.screen_shoot(self.driver,"delete_album")

        value = self.album.newalbumname
        value2 = self.album.getpagecode()
        try:

            self.assertNotIn(value, value2)

        except Exception:
            testalbum_log.action_log.exception(f'断言失败，案例不通过---------{value}不在当前页面')
            raise

        else:
            testalbum_log.action_log.info(f'断言成功，案例通过，当前页面网址-----------{value}在当前页面')





if __name__=="__main__":
    unittest.main()