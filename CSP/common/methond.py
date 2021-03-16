import logging
from config import Conf
from common.my_log import Log
import requests
import os,sys,json
Api_log = Log(__name__,file=logging.INFO,cmd=logging.INFO)



payload = {'key1': 'value1', 'key2': 'value2'}
r =requests.get('http://httpbin.org/get',params=payload)
#源码解析
'''
发送一个get请求、
params：查询字符串，以字符串字段，元组传递参数
'''
#获取完整的请求路径
value =r.url

if __name__=="__main__":
 print()