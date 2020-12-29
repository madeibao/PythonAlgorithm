from typing import List

给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
返回值小于或等于 bound 的所有强整数组成的列表。
你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

#===============================
# 输入：x = 2, y = 3, bound = 10
# 输出：[2,3,4,5,7,9,10]
# 解释：
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 7 = 2^2 + 3^1
# 5 = 2^1 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2


# 下面的方法会超时。
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        list2 = []

        def true2(m, n, num):
            for i in range(num//2+1):
                for j in range(num//2+1):
                    if m**i+n**j == num:
                        return True
            return False
        for i in range(1, bound+1):
            if true2(x, y, i):
                list2.append(i)

        return list2

#math.floor是下取整
#math.log是取对数的值。


import math
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a_list = []
        x_num = math.floor(math.log(bound,x)) if x != 1 else 1
        y_num = math.floor(math.log(bound,y)) if y != 1 else 1
        for item in range(x_num+1):
            for i in range(y_num+1): 
                num = x ** item + y ** i
                if num <= bound:
                    a_list.append(num)
        return list(set(a_list))


# 方法3

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x==1 and y==1 and bound>=2:
            return [2]
        if x==1 and y==1 and bound<2:
            return None
        res=[]
        if x==1 or y==1:
            c=max(x,y)
            m=0
            while c**m+1<=bound:
                res.append(c**m+1)
                m+=1
            return res
        
        a=0
        b=0
        while x**a+y**b<=bound:
            while x**a+y**b<=bound:
                if x**a+y**b not in res:
                    res.append(x**a+y**b)
                b+=1
            a+=1
            b=0
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.powerfulIntegers(2, 3, 10))



