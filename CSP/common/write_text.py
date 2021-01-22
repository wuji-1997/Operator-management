# -- coding: utf-8 --

from config import Conf
from common.my_log import Log
import logging
import time
text_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)

class Text_action(object):


     def __init__(self,file_path):

         self.name = file_path


     def read_file(self):
         """

         :return:
         """
         with open(self.name,'r',encoding='utf-8') as fp:

             for line in fp.readlines():
                 print(line)

     def write_file(self,value):
         """

         :return:
         """
         now = time.strftime('%Y-%m-%d %H:%M:%S')
         with open(self.name,'a',encoding='utf-8') as ft:
             ft.write('\n'+now+'------'+value)
             ft.close()

if __name__=="__main__":
    test = Text_action(Conf.notebook+r'\notebook.txt')
    test.write_file('第一个记事本')
    test.read_file()