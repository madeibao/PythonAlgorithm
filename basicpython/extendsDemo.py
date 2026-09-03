# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/3/星期四 10:51
# @File: extendsDemo

class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):  # 多继承
    pass

if __name__ == '__main__':
    print(C().greet());
    # 从左向右的顺序，找到哪个是哪个