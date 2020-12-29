
# 给定一个不重复的列表的元素内容，然后求出列表元素的所有的内容的全排列。


from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(set(itertools.permutations(nums)))


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 1, 2]))

# [(1, 2, 1), (2, 1, 1), (1, 1, 2)]















