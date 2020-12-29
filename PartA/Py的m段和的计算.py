

# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/6/9 9:21
# @File: Test.py


# 【小米2018-09-20在线笔试】最优分割


题目描述
依次给出n个正整数A1，A2， …，An，将n个数分割成m段，每一段内的所有数的和记为这一段的权重，m段权重的最大值记为本次分割的权重。问所有分割方案中分割权重的最小值是多少？

输入

第一行依次给出正整数n，m，单空格切分；（n<=10000，m<=10000，m<=n）

第二行依次给出n个正整数单空格切分A1，A2，…，An（Ai<=10000）

输出

分割权重的最小值

样例输入

5 3

1 4 2 3 5

样例输出

5

Hint

分割成 14 | 2 3 | 5 的时候，3段的权重都为5，得到分割权重的最小值。
————————————————
版权声明：本文为CSDN博主「阿木寺」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/amusi1994/article/details/82793562

#================================================================
#=--------------------------------------------------------------------------------


def splitArrays(arrays, m):
    top = sum(arrays)  # 确定上界
    down = top // m  # 确定下界 （下取整）
    size = len(arrays)
    while down <= top:
        mid = (down + top) // 2  # （下取整）
        n = m
        cnt = 0
        flag = True
        for x in range(size):
            if arrays[x] > mid:  # 如果发现数列里面有一个大于目标解的，说明真正的解在右区间，即继续搜索右区间
                flag = False
                break
            if cnt + arrays[x] > mid:  # 进行一次分割， 并初始化 n, cnt
                n -= 1
                cnt = 0
            cnt += arrays[x]  # 统计每次分割的小区间的和，
            if n == 0:  # n == 0 说明划分的段数超过了 m，说明真正的解在右区间，即继续搜索右区间
                flag = False
                break

        if flag:  # 确定下一个要搜索的区间范围
            top = mid - 1  # flag == True 说明最优解还可以再小，即在左区间里面
        else:
            down = mid + 1
    return down


if __name__ == '__main__':
    m_n = list(map(int, input("").split()))
    n, m = m_n[0], m_n[1]
    arrays = list(map(int, input("").split()))
    print(splitArrays(arrays, m))

