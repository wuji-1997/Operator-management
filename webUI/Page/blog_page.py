from webUI.common.my_log import Log
import logging
from webUI.Page.base_page import BasePage
from webUI.common.readexcel import ReadExcel
from webUI.config.Conf import *
import time

blog_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

blog_excel = ReadExcel(filepath=excel_path+r'\test_iwebsns.xlsx',sheet_name='blog')

class BlogPage(BasePage):


    blogbutton = [blog_excel.getexcelvalue(1,3),blog_excel.getexcelvalue(1,4)]   #日志按钮
    newblog = [blog_excel.getexcelvalue(3,3),blog_excel.getexcelvalue(3,4)]  #点击新建日志按钮

    blogtilte=[blog_excel.getexcelvalue(4,3),blog_excel.getexcelvalue(4,4),blog_excel.getexcelvalue(4,5)]  #日志标题
    addsort = [blog_excel.getexcelvalue(5,3),blog_excel.getexcelvalue(5,4),  #日志分类
               blog_excel.getexcelvalue(6,3),blog_excel.getexcelvalue(6,4),blog_excel.getexcelvalue(6,5),   #输入新的分类
               blog_excel.getexcelvalue(7,3),blog_excel.getexcelvalue(7,4),   #确认添加日志分类
               blog_excel.getexcelvalue(8,3),blog_excel.getexcelvalue(8,4),blog_excel.getexcelvalue(8,5)]  #下拉框选择
    blog_text = [blog_excel.getexcelvalue(10,3),blog_excel.getexcelvalue(10,4),blog_excel.getexcelvalue(10,5)]  #日志内容
    button=(blog_excel.getexcelvalue(12,3),blog_excel.getexcelvalue(12,4))

    blogtag = [blog_excel.getexcelvalue(13,3),blog_excel.getexcelvalue(13,4),blog_excel.getexcelvalue(13,5)]  #日志标签


    deleteblog = [blog_excel.getexcelvalue(14,3),blog_excel.getexcelvalue(14,4)]
    deletebutton = [blog_excel.getexcelvalue(15,3),blog_excel.getexcelvalue(15,4)]

    changeblog = [blog_excel.getexcelvalue(16,3),blog_excel.getexcelvalue(16,4)]

    newtitle=blog_excel.getexcelvalue(17,5)


    def intoform(self):
        """
        进入内置表单
        :return:
        """
        self.click_element(self.blogbutton[0],self.blogbutton[1])
        self.handleform(0)
        blog_log.action_log.info("进入日志的内置表单")

    def intoblog(self,blog):
        """
        进入已经存在的日志
        :return:
        """
        self.intoform()
        self.click_element(self.deleteblog[0],value=blog)
        self.wait(3)


    def new_blog(self):
        """
        新增功能
        :return:
        """
        self.intoform()
        self.wait(2)
        self.click_element(self.newblog[0],self.newblog[1])

        self.input_value(self.blogtilte[0],self.blogtilte[1],self.blogtilte[2])

        self.input_value(self.blogtag[0],self.blogtag[1],self.blogtag[2])

        self.click_element(self.addsort[0],self.addsort[1])
        time.sleep(1)
        self.input_value(self.addsort[2],self.addsort[3],self.addsort[4])
        time.sleep(1)

        self.click_element(self.addsort[5],self.addsort[6])
        time.sleep(3)

        self.handle_select(self.addsort[7],self.addsort[8],self.addsort[9])
        time.sleep(2)
        self.handleform(0)
        time.sleep(3)
        self.input_value(self.blog_text[0],self.blog_text[1],self.blog_text[2])
        self.parentform()
        time.sleep(3)
        self.click_element(self.button[0],self.button[1])


    def delete_blog(self):
        """
        删除功能
        :return:
        """
        self.intoblog(blog=self.newtitle)
        self.click_element(self.deletebutton[0],self.deletebutton[1])
        self.wait(3)
        self.handlealert()
        self.wait(3)
        self.click_element(self.blogbutton[0],self.blogbutton[1])
        self.wait(3)

    def change_blog(self):
        """
        日志信息变更
        :return:
        """
        self.intoblog(blog=self.blogtilte[-1])
        self.click_element(self.changeblog[0],self.changeblog[1])
        self.wait(3)
        self.clear_input(self.blogtilte[0],self.blogtilte[1])
        self.wait(2)
        self.input_value(self.blogtilte[0],self.blogtilte[1],self.newtitle)

        self.wait(2)
        self.click_element(self.button[0],self.button[1])
        self.wait(2)
        self.click_element(self.blogbutton[0],self.blogbutton[1])
        self.wait(3)






