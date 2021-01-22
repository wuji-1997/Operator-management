# -- coding: utf-8 --

import logging
import time





class Log(object):


    def __init__(self,name,file=logging.INFO,cmd=logging.INFO):
        """
        构造日志收集器
        :param name: 收集器名称
        :param file: 文件输出渠道日志等级
        :param cmd: 控制台输出日志等级
        """
        self.csp_log = logging.getLogger(name)
        self.csp_log.setLevel(logging.DEBUG)

        logtime = time.strftime('%Y-%m-%d')

        fmt =logging.Formatter('%(asctime)s-%(filename)s:[%(lineno)s]-[%(levelname)s]-%(message)s')  #日志输出格式

        filename =r'E:\CSP\log\my_log'+'\log' +'-'+logtime +'.log'   #输出日志文件地址

        fh = logging.FileHandler(filename,encoding='utf-8')
        fh.setLevel(file)
        fh.setFormatter(fmt)

        ch = logging.StreamHandler()
        ch.setLevel(cmd)
        ch.setFormatter(fmt)

        self.csp_log.addHandler(fh)
        self.csp_log.addHandler(ch)


if __name__=="__main__":

    test = Log('wuji',file=logging.INFO,cmd=logging.INFO)
    test.csp_log.info('这是一个info日志')




