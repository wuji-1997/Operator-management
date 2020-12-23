#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'wuji'


import configparser
from webUI.common.my_log import Log
import logging
import os
from webUI.config import Conf


readini_log  = Log(__name__,file=logging.INFO,cmd=logging.INFO)


class Readini(object):


    def __init__(self):

        self.readconfig = configparser.ConfigParser()


    def get_configvalue(self,filepath,section_name,option_name):
        try:
            self.readconfig.read(filepath,encoding='utf-8')
            value =self.readconfig.get(section_name,option_name)

        except Exception:
            readini_log.action_log.exception(f'从配置文件{filepath}中读取数据失败')
            raise
        else:
            readini_log.action_log.info(f'从配置文件{filepath}中读取数据成功')
            return value

if __name__=="__main__":
   test = Readini()
   value = test.get_configvalue(os.path.join(Conf.current_path,'config.ini'),section_name='project',option_name='project_path')
   value2 = test.get_configvalue(os.path.join(Conf.current_path,'config.ini'),section_name='user',option_name='from')
   value3 = test.get_configvalue(os.path.join(Conf.current_path,'config.ini'),section_name='user',option_name='subject')
   print(value,'\n',value2,'\n',value3)
