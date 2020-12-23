# -- coding: utf-8 --
import smtplib  #发送邮件模板
from email.mime.text import MIMEText  #构建邮件内容
from email.header import Header#定义邮件标题
from email.mime.multipart import MIMEMultipart#用于传送附件
import email
from webUI.config.Conf import *
from webUI.common.my_log import Log
import os
import logging
read_email = Readini()
email_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)
'''
smtplib模块主要负责发送邮件：是一个发送邮件的动作，连接服务器，登录邮箱、发送邮件(发件人、收件人、邮箱内容)
email模块主要负责构造邮件：指的是邮箱页面显示的一些构造，如发件人，收件人，主题，正文，附件等
'''

class sendSmptEmail():


    frompassword=read_email.get_configvalue(os.path.join(current_path,'config.ini'),section_name='user',option_name='password')
    fromemail = read_email.get_configvalue(os.path.join(current_path,'config.ini'),'user','from')
    toemail = read_email.get_configvalue(os.path.join(current_path,'config.ini'),'user','to')
    emailsubject = read_email.get_configvalue(os.path.join(current_path,'config.ini'),'user','subject')
    server = read_email.get_configvalue(os.path.join(current_path,'config.ini'),'user','HOST_SERVER')

    def send_email(self):
        """

        :param lastest_report:
        :return:
        """

        #邮箱配置
        server_host = self.server   #邮箱服务端
        user = self.fromemail       #邮件发件人账号
        pws = 'PIZKIJFZMTNWUHXX'     #邮件发件人密码
        receiver = self.toemail     #收件人邮箱账号
        email_subject = self.emailsubject   #发送邮箱主题


        #发送邮件格式
        mail_content = "这是一份自动发送的邮件"


        msg = MIMEMultipart()


        msg['Subject'] = Header(email_subject,'utf-8')  #邮件主题
        msg['To'] = receiver
        msg['From']=user
        msg.attach(MIMEText(mail_content,'html','utf-8'))

        try:
            smtp = smtplib.SMTP_SSL(server_host, port=465)  # 连接服务
            smtp.set_debuglevel(1)  # 0是关闭，1是开启debug
            smtp.login(user, pws)  # 登录，需要传入用户名和授权码
            smtp.sendmail(user,receiver,msg.as_string())
            smtp.quit()

        except Exception:
            email_log.action_log.exception('邮件发送失败')
            raise
        else:
            email_log.action_log.info('邮件发送成功')


if __name__=='__main__':
    test_email = sendSmptEmail()
    test_email.send_email()







