

from functools import cmp_to_key

def cmp(a, b):
    # 返回负数 a<b, 0 相等, 正数 a>b
    if a % 2 != b % 2:
        return -1 if a % 2 else 1   # 奇数排前
    return a - b


print(sorted([5, 2, 8, 3], key=cmp_to_key(cmp)))
