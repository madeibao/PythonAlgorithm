# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2019/8/15 14:25
# @File: Main.py


def change(name):
    result = name[0:1].upper()+name[1:len(name)].lower()
    return result


name_list = ['kzd', 'ysy', 'kcw', 'scr', 'ky']   # 将首字母大写，其余字母小写。
name_li = list(map(change, name_list))
print(name_li)





