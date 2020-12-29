

# 四个数字来组成的时间的最大的是。
# leetcode949

from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort(reverse=True)
        for a,  b, c, d in permutations(A):
            if a*10+b <24 and c*10+d<60:
                return f"{a}{b}:{c}{d}"
        return ''

if __name__ == '__main__':
     s = Solution()
     list2 = [1, 2, 3, 4]
     print(s.largestTimeFromDigits(list2))





