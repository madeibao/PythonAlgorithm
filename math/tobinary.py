# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/20/星期日 17:30
# @File: tobinary


def to_binary(n):
    stack = []
    while n > 0:
        stack.append(n % 2)
        n //= 2
    return ''.join(str(stack.pop()) for _ in range(len(stack)))

if __name__ == '__main__':
    print(to_binary(1))
    print(to_binary(10))  # 1010