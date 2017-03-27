# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import os
import bs4
__author__ = '刘宇威'
__date__ = 2017 / 3 / 18


class BusinessAttribute:
    def __init__(self, tag):
        self.__alias = tag['alias']
        self.__name = tag['name']
        self.__dataType = tag['STRING']
        self.__type = tag['ENTITY']

    def get_alias(self):
        return self.__alias

    def get_name(self):
        return self.__name

    def get_dataType(self):
        return self.__dataType

    def get_type(self):
        return self.__type

    def __str__(self):
        """
                用str()时调用
                :return:
                """
        res = "alias: %s\n" % self.__alias \
            + "name: %s\n" % self.__name \
            + "dataType: %s\n" % self.__dataType \
            + "Type: %s\n" % self.__type
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


class BusinessObject:
    """
    类实例，记录实例的对应下标，从 1 开始
    """
    __BusinessObject_index = 0

    def __init__(self, tag):
        def __get_index():
            """
            下标自增并返回下标
            :return :
            """
            BusinessObject.__BusinessObject_index += 1
            return BusinessObject.__BusinessObject_index

        def init_business_attribute(tags):
            paras = []
            for tag in tags:
                paras.append(BusinessAttribute(tag))
            return paras
        self.__name = tag['name']
        self.__alias = tag['alias']
        self.__business_attribute_list = init_business_attribute(tag.find_all("BUSINESS_ATTRIBUTE"))
        self.__index = __get_index()

    def get_alias(self):
        return self.__alias

    def get_name(self):
        return self.__name

    def get_business_attribute_list(self):
        return self.__business_attribute_list[:]

    def get_index(self):
        return self.__index

    def __str__(self):
        """
        用str()时调用
        :return:
        """
        res = "--------business attribute info-----------\n" \
            + "alias: %s\n" % self.__alias \
            + "name: %s\n" % self.__name + "--------para info-----------\n"
        for attribute in self.__business_attribute_list:
            res += str(attribute) + "-------------------\n"
        return res + '\n'


class BusinessObjectAnalyzer:
    """
    分析BusinessObject
    ① 是否 Para 没有属性
    ② 是否 Para 有重复的属性
    """
    # to be continue


def get_file_list(cur_dir, file_list):
    """
    :param cur_dir:
    :param file_list:
    :return:
    """
    if os.path.isfile(cur_dir):
        file_list.append(cur_dir)
    elif os.path.isdir(cur_dir):
        for s in os.listdir(cur_dir):
            new_dir = os.path.join(cur_dir, s)
            get_file_list(new_dir, file_list)
    return file_list


def read_xml(file):
    """  
    先决条件：
        本地的文件是 utf-8 编码的，同时需要预处理 &.*; ，将这种正则表达式的内容清除
        读取本地 xml 文件并返回 beautifulsoup4 的对象
        xml 文件只有一行
    :return: 页面内容
    """
    print(file)
    with open(file, 'r', encoding='utf8') as file_reader:
        response = file_reader.readlines()
        # response = ''.join(response)
        response = response[0]
    print(response)
    print('')
    bs_obj = bs4.BeautifulSoup(response, "lxml")
    print(bs_obj.find_all('business_theme'))
    return bs_obj


def get_business_objects(bs_obj):
    business_object_list = []
    business_object_tag_list = bs_obj.find_all("BUSINESS_OBJECT")
    print('bussiness object cnt is %s' % len(business_object_tag_list))
    for business_object_tag in business_object_tag_list:
        business_object = BusinessObject(business_object_tag)
        business_object_list.append(business_object)
    return business_object_list


def main():
    dir = "D:/intern in FIRE/BI/3. 数据探索/exporttheme"
    files = get_file_list(dir, [])
    for file in files:
        bs_obj = read_xml(file)
        # print(bs_obj)
        business_object_list = get_business_objects(bs_obj)
        business_object_without_attribute_list = []
        business_object_with_duplicate_attribute = []
        business_attribute_name_set = set()
        for business_object in business_object_list:
            # you need write code here.
            pass
            # business_attributes = business_object.get_business_attribute_list()
            # for business_attribute in business_attributes:
            #     business_attribute_name_set.add(business_attribute.get_name())


if __name__ == '__main__':
    main()
