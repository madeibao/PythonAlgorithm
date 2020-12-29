
from typing import List, Tuple

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1] # 下三角
        for i in range(len(a) - 2, -1, -1): 
            tmp *= a[i + 1] # 上三角
            b[i] *= tmp # 下三角 * 上三角
        return b

if __name__ == "__main__":
    s = Solution()
    list2 = [1,2,3,4,5]
    print(s.constructArr(list2))

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

class Solution(object):
    def constructArr(self, a):
        if len(a)==0:
            return 0
        left = [0]*len(a)
        right = [0]*len(a)
        res = [0]*len(a)

        left[0] = 1
        right[len(a)-1] = 1
        for i in range(1, len(a)):
            left[i] = left[i-1] * a[i-1]

        for j in range(len(a)-2, -1, -1):
            right[j] = right[j+1] * a[j+1]

        for i in range(len(a)):
            res[i] = left[i] * right[i]

        return res


if __name__ == "__main__":
    s = Solution()
    list2 = [1, 2, 3, 4, 5]
    print(s.constructArr(list2))
