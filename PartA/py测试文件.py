# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:29:02 2020

@author: ASUS
"""

import math
list2 = list(map(int, input().split(" ")))

R = list2[0]

one = [list2[1], list2[2]]
two = [list2[3], list2[4]]
three = [list2[5], list2[6]]

enemy = [list2[7], list2[8]]

def func(a, b):
    len2 = abs(a[0] - b[0])
    len3 = abs(a[1] - b[1])

    return int(math.sqrt(len2**2+len3**2))


res = 0
if func(one, enemy)<=R:
    res +=1

if func(two,enemy)<=R:
    res += 1

if func(three,enemy)<=R:
    res += 1

if res<=0:
    print("0x")
else:
    print(str(res)+"x")



    

