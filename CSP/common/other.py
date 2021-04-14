# -- coding: utf-8 --
import os
from config import Conf
from common.my_log import Log
import logging
delete_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)
import time
import locale

def delete_file(filepath):
    """
    删除文件
    :param filepath:
    :return:
    """
    file  = os.listdir(filepath)

    for i in file:
        deletefile =os.path.join(filepath,i)

        if os.path.isdir(deletefile):
            delete_file(deletefile)
            delete_log.csp_log.info(f'THE file of {filepath} 已清空')
        else:
            os.remove(deletefile)
            delete_log.csp_log.info(f'删除{deletefile}成功')

def create_dir(filepath):
    """
    创建目录若目录不在则自动创建
    :param filepath:
    :return:
    """
    locale.setlocale(locale.LC_CTYPE,'chinese')
    now_date = time.strftime('%Y年%m月%d日')
    newfile = filepath+r'\new'+now_date
    is_exist_file = os.path.exists(newfile)
    if not is_exist_file:
        os.makedirs(filepath+now_date)
        delete_log.csp_log.info(f'文件夹{newfile}创建成功')
        return True
    else:
        delete_log.csp_log.info(f'文件夹{newfile}已经存在创建失败')
        return False



if __name__=="__main__":
   delete_file(filepath=Conf.test_screenshoot+r'\customer')
   delete_file(filepath=Conf.test_screenshoot+r'\chatbot')
   delete_file(filepath=Conf.test_screenshoot+r'\csp')
   delete_file(filepath=Conf.test_screenshoot + r'\login')
   #delete_file(filepath=Conf.test_screenshoot + r'\update_password')
   delete_file(filepath=Conf.test_screenshoot + r'\system')
   delete_file(filepath=Conf.testreport)
   #delete_file(filepath=Conf.log_path)
