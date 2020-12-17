import logging
import time




class Log(object):


    def __init__(self,name,file=logging.INFO,cmd=logging.INFO):
        """

        :param name:
        :param file:
        :param cmd:
        """
        self.action_log = logging.getLogger(name)   #定义日志收集器
        self.action_log.setLevel(logging.DEBUG)     #设置日志收集的等级

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(levelno)s] - %(levelname)s -%(lineno)d- %(message)s') #设置日志输出格式
        log_time = time.strftime('%Y-%m-%d')

        log_path = r'D:\webapp\webUI\LOG\log\log' + log_time+'.log'

        #添加日志输出渠道

        filesh = logging.FileHandler(log_path,encoding='utf-8')
        filesh.setLevel(file)
        filesh.setFormatter(fmt)

        cmdsh = logging.StreamHandler()
        cmdsh.setFormatter(fmt)
        cmdsh.setLevel(cmd)

        self.action_log.addHandler(filesh)
        self.action_log.addHandler(cmdsh)

if __name__=='__main__':
    testlog=Log('wuji',file=logging.INFO,cmd=logging.INFO)

    testlog.action_log.info("这是一个info日志")
    testlog.action_log.error("这是一个error日志")
    testlog.action_log.debug("这是一个debug日志")
    testlog.action_log.warning("这是一个warning日志")





