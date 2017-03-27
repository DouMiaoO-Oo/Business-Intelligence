# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import os
import bs4
__author__ = '刘宇威'
__date__ = 2017 / 3 / 23

who = {'谁'}
what = {"哪些", "那些", "哪个", "什么", "多少", "几"}
when = {'什么时候', '几时'}
where = {"哪里", "哪儿", '什么地方'}
why = {'为什么', '为何'}
how = {'怎么'}
interrogative_focus = set()
interrogative_focus |= who
interrogative_focus |= what
interrogative_focus |= when
interrogative_focus |= where
interrogative_focus |= why
interrogative_focus |= how


def my_contains(sent):
    for item in interrogative_focus:
        if item in sent:
            return True
    return False


def main():
    """
    利用疑问词判断是打开报表还是数据探索
    :return: 
    """
    stop = False
    while stop is False:
        sent = input("请输入句子, \"stop\"为退出:\n")
        if sent.lower() == "stop":
            stop = True
        if my_contains(sent):
            print("数据探索")
        else:
            print("打开报表")


if __name__ == '__main__':
    main()
