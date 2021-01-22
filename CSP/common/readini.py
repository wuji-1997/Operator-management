# -- coding: utf-8 --
import configparser
import logging
from common.my_log import Log
import os
from config import Conf
readini_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)


class Readini(object):


    def __init__(self):

        self.config = configparser.ConfigParser()

    def get_value(self,filepath,sectionname,optionname):
        """
        读取配置文件数据
        :param filepath:配置文件
        :param sectionname:
        :param optionname:
        :return:
        """
        try:
            self.config.read(filepath,encoding='utf-8')
            value = self.config.get(sectionname,optionname)

        except Exception:
            readini_log.csp_log.exception(f'from {filepath} get value:[{value}]----- failed')
            raise

        else:
            readini_log.csp_log.info(f'from {filepath} get value:["{value}"]---- successed')
            return value


if __name__=="__main__":
    test = Readini()

    value = Readini().get_value(os.path.join(Conf.current_path,'config.ini'),'test_url','url1')

    print(value)

