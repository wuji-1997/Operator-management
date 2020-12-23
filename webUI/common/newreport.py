
from webUI.config.Conf import *

#存放测试报告的位置

report_dir = report_path


def Latest_report(report_dir):
    """
    返回最新的测试报告文件
    :param report_dir:
    :return:
    """
    # os.listdir()方法用于返回指定文件夹包含文件或文件名字列表
    lists = os.listdir(report_dir)

    # 按照时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    file = os.path.join(report_dir, lists[-1])
    return file

