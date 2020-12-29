
from typing import List
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort(reverse=True)
        for a, b, c, d, e, f in permutations(A):
            if a*10+b <24 and c*10+d<60 and e*10+f<60:
                return f"{a}{b}:{c}{d}:{e}{f}"
        return ''


if __name__ == '__main__':
    s = Solution()
    list2 = [1, 2, 3, 4, 8, 9]
    print(s.largestTimeFromDigits(list2))


