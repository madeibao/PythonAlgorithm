
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        list2 = []
        for i in points:
            list2.append(((i[0]*i[0])+(i[1]*i[1]))**0.5)
        list3 = sorted(list2)[:K]
        list4 = []
        for i in points:
            if ((i[0]*i[0])+(i[1]*i[1]))**0.5 in list3:
                list4.append(i)
        return list4

# 方法二

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def msort(point):
            return point[0]**2 + point[1]**2
        points.sort(key=msort)  # 内部的自定义的函数内容。
        return points[:K]


# sort结合匿名函数的用法来更好的实现排序的内容。
class Solution:
    def kClosest(self, points, K) :
        a = lambda x :x[0]**2 + x[1]**2
        points.sort(key = a)
        return points[:K]





if __name__ == '__main__':
    s = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(s.kClosest(points, k))