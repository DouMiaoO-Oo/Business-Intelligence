# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import os
import bs4
__author__ = '刘宇威'
__date__ = 2017 / 3 / 18


class Para:
    """
    打开报表 xml 的 <Para> 标签
    """
    def __init__(self, tag):
        self.__alias = tag['alias']
        self.__name = tag['name']
        self.__isrequired = tag['isrequired']

    def get_alias(self):
        return self.__alias

    def get_name(self):
        return self.__name

    def get_isrequired(self):
        return self.__isrequired

    def __str__(self):
        """
                用str()时调用
                :return:
                """
        res = "alias: %s\n" % self.__alias \
            + "name: %s\n" % self.__name \
            + "isrequired: %s\n" % self.__isrequired
        return res

    def __hash__(self):
        """
        将对象的实例放入 set 中时会调用该方法
        :return: hash 后的值
        """
        return hash((self.__alias, self.__name))
        # return hash(self.__alias)
        # return hash(self.__name)

    def __eq__(self, other):
        """
        将对象的实例放入 set，如果两个对象的 hash 值相同时，会调用该方法
        :param other: 另一个 Para 对象
        :return: 是否相等
        """
        return (self.__alias == other.__alias) and (self.__name == other.__name)


class Report:
    """
    打开报表 xml 的 <Report> 标签
    类实例，记录实例的对应下标，从 1 开始
    """
    __Report_index = 0

    def __init__(self, tag):
        def __get_index():
            """
            下标自增并返回下标
            :return :
            """
            Report.__Report_index += 1
            return Report.__Report_index

        def init_paras(tags):
            paras = []
            for tag in tags:
                paras.append(Para(tag))
            return paras
        self.__aliaspath = tag['aliaspath']
        self.__path = tag['path']
        self.__alias = tag['alias']
        self.__name = tag['name']
        self.__para_list = init_paras(tag.find_all("param"))
        self.__index = __get_index()

    def get_alisapath(self):
        return self.__aliaspath

    def get_path(self):
        return self.__path

    def get_alias(self):
        return self.__alias

    def get_name(self):
        return self.__name

    def get_para_list(self):
        return self.__para_list[:]

    def get_index(self):
        return self.__index

    def __str__(self):
        """
        用str()时调用
        :return:
        """
        res = "--------report info-----------\n" + "aliaspath: %s\n" % self.__aliaspath \
            + "path: %s\n" % self.__path \
            + "alias: %s\n" % self.__alias \
            + "name: %s\n" % self.__name + "--------para info-----------\n"
        for para in self.__para_list:
            res += str(para) + "-------------------\n"
        return res + '\n'


class ReportAnalyzer:
    """
    分析报表
    ① 是否 Para 没有属性
    ② 是否 Para 有重复的属性
    """
    def __init__(self, report=None):
        self.__report = report

    def set_report(self, report):
        self.__report = report

    def report_has_no_para(self):
        return len(self.__report.get_para_list()) == 0

    def report_has_duplicate_para(self):
        detector = set()
        for para in self.__report.get_para_list():
            if para in detector:
                return False
            else:
                detector.add(para)
        return True


def read_xml(file):
    """  读取本地 xml 文件并返回 beautifulsoup4 的对象
        xml 文件只有一行
    :return: 页面内容
    """
    with open(file, 'r', encoding='utf8') as file_reader:
        response = file_reader.readlines()
        response = ''.join(response)
    bs_obj = bs4.BeautifulSoup(response, "lxml")
    return bs_obj


def get_reports(bs_obj):
    report_list = []
    report_tag_list = bs_obj.find_all("report")
    for report_tag in report_tag_list:
        report = Report(report_tag)
        report_list.append(report)
    return report_list


def main():
    """
    需要确认 xml 文件的路径
    即修改 file 的值
    :return:
    """
    # file = "D:/intern in FIRE/BI/2. 打开报表/reports.xml"
    file = "D:/intern in FIRE/BI/2. 打开报表/旧版本exportreport/reports.xml"
    bs_obj = read_xml(file)
    report_list = get_reports(bs_obj)
    para_name_set = set()

    report_without_para_list = []
    report_with_duplicate_para = []
    report_analyser = ReportAnalyzer()
    for report in report_list:
        report_analyser.set_report(report)
        paras = report.get_para_list()
        for para in paras:
            para_name_set.add(para.get_name())
        if report_analyser.report_has_no_para() is True:
            report_without_para_list.append(str(report.get_index()))
        elif report_analyser.report_has_duplicate_para() is False:
            report_with_duplicate_para.append(str(report.get_index()))
        else:
            pass

    print("report has --no-- <Para> tag")
    print(report_without_para_list)
    print("report has ***duplicate*** <Para> tag")
    print(report_with_duplicate_para)
    # 写回分析的结果
    # with open('result.txt', 'w', encoding='utf8') as write_file:
    #     write_file.writelines('\n'.join(list(para_name_set)))

if __name__ == '__main__':
    main()
