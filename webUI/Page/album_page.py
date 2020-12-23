from webUI.common.my_log import Log
import logging
from webUI.Page.base_page import BasePage
from webUI.common.readexcel import ReadExcel
from webUI.config.Conf import *
import time


album_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

album_excel = ReadExcel(filepath=excel_path+r'\test_iwebsns.xlsx',sheet_name='album')


class AlbumPage(BasePage):

    albumbutton = [album_excel.getexcelvalue(1,3),album_excel.getexcelvalue(1,4)]
    newalbum = [album_excel.getexcelvalue(3,3),album_excel.getexcelvalue(3,4)]
    albumname = [album_excel.getexcelvalue(4,3),album_excel.getexcelvalue(4,4),album_excel.getexcelvalue(4,5)]
    albummsg = [album_excel.getexcelvalue(5,3),album_excel.getexcelvalue(5,4),album_excel.getexcelvalue(5,5)]
    albumtag = [album_excel.getexcelvalue(6,3),album_excel.getexcelvalue(6,4),album_excel.getexcelvalue(6,5)]
    button = [album_excel.getexcelvalue(7,3),album_excel.getexcelvalue(7,4)]

    uploadbutton = [album_excel.getexcelvalue(8,3),album_excel.getexcelvalue(8,4)]
    selectalbum=[album_excel.getexcelvalue(9,3),album_excel.getexcelvalue(9,4),album_excel.getexcelvalue(9,5)]
    uplaodway = [album_excel.getexcelvalue(10,3),album_excel.getexcelvalue(10,4)]
    startupload = [album_excel.getexcelvalue(11,3),album_excel.getexcelvalue(11,4),album_excel.getexcelvalue(11,5)]
    affirm = [album_excel.getexcelvalue(12,3),album_excel.getexcelvalue(12,4)]

    deletealbum = [album_excel.getexcelvalue(13,3),album_excel.getexcelvalue(13,4)]

    updatealbum = [album_excel.getexcelvalue(15,3),album_excel.getexcelvalue(15,4)]
    newalbumname = album_excel.getexcelvalue(16,5)
    changebutton=(album_excel.getexcelvalue(17,3),album_excel.getexcelvalue(17,4))




    def  intoform(self):
        """
        进入相册内置表单
        :return:
        """
        self.click_element(self.albumbutton[0],self.albumbutton[1])

        self.handleform(0)
        album_log.action_log.info(f'进入相册内置表单')


    def new_album(self):
        """
        新建相册
        :return:
        """
        self.intoform()
        self.click_element(self.newalbum[0],self.newalbum[1])
        self.wait(1)
        self.input_value(self.albumname[0],self.albumname[1],self.albumname[2])
        self.wait(1)
        self.input_value(self.albummsg[0],self.albummsg[1],self.albummsg[2])
        self.wait(1)
        self.input_value(self.albumtag[0],self.albumtag[1],self.albumtag[2])
        self.wait(1)
        self.click_element(self.button[0],self.button[1])
        self.wait(1)
        self.click_element(self.albumbutton[0],self.albumbutton[1])

    def upload_pictures(self):
        """
        上传图片
        :return:
        """
        self.intoform()
        self.click_element(self.uploadbutton[0],self.uploadbutton[1])

        self.wait(2)

        self.handle_select(self.selectalbum[0],self.selectalbum[1],self.selectalbum[2])
        self.wait(2)

        self.click_element(self.uplaodway[0],self.uplaodway[1])
        self.wait(2)

        self.input_value(self.startupload[0],self.startupload[1],self.startupload[2])
        self.wait(2)

        self.click_element(self.affirm[0],self.affirm[1])
        self.wait(2)


    def delete_album(self):
        """
        删除相册
        :return:
        """
        self.intoform()
        self.click_element(self.deletealbum[0],self.deletealbum[1])
        self.wait(2)
        self.handlealert()
        self.click_element(self.albumbutton[0],self.albumbutton[1])
        self.wait(2)

    def update_album(self):
        """
        更新相册
        :return:
        """
        self.intoform()
        self.click_element(self.updatealbum[0],self.updatealbum[1])
        self.wait(2)
        self.clear_input(self.albumname[0],self.albumname[1])
        self.wait(2)
        self.input_value(self.albumname[0],self.albumname[1],self.newalbumname)
        self.wait(2)
        self.click_element(self.changebutton[0],self.changebutton[1])
        self.wait(2)
        self.click_element(self.albumbutton[0],self.albumbutton[1])

