from typing import List

class Solution(object):
    def arraysIntersection(self, arr1:List, arr2:List, arr3:List) -> List :
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        val = [0] * 30
        for i in arr1:
            val[i] += 1
        for i in arr2:
            val[i] += 1
        for i in arr3:
            val[i] += 1
        res = []

        for i,v in enumerate(val):
            if v == 3:res.append(i)
        return res


if __name__ == "__main__":
    s= Solution()
    arra = [1,2,3,4,5]
    arrayB = [1,2,5,7,9]
    arrc = [1,3,4,5,8]
    res = s.arraysIntersection(arra, arrayB, arrc)
    print(res)

