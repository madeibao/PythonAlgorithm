# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2019/10/6 9:17
# @File: Test.py


# 最长的有效的密码内容:
# ABBA

# ABBA->12ABBA,ABA->ABAKK,

while True:
    try:
        def count_sym(s):
            length = len(s)
            list_s = []
            for i in range(length - 1):
                if s[i] == s[i + 1]:
                    count = 2
                    key = 2 * i + 1
                    while i - 1 >= 0 and key - i + 1 <= length - 1:
                        i = i - 1
                        if s[i] != s[key - i]:
                            break
                        count += 2
                    list_s.append(count)
                try:
                    if s[i] == s[i + 2]:
                        count = 3
                        key = 2 * i + 2
                        while i - 1 >= 0 and key - i + 1 <= length - 1:
                            i = i - 1
                            if s[i] != s[key - i]:
                                break
                            count += 2
                        list_s.append(count)
                except IndexError:
                    continue
            return max(list_s)

        str2 = input()
        print(count_sym(str2))

    except:
        break





