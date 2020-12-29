
from typing import List
import itertools


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        dic = {}
        for i in range(len(nums) + 1):
            for each in itertools.combinations(nums, i):
                each = tuple(sorted(each))   # 变成元组内容，字典的键是不可以修改的，而值是可以修改的。
                if each not in dic:
                    res.append(each)
                    dic[each] = 1   # 代表的是出现了一次的内容。
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2, 3]))



#============================================================================
[(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 2), (2, 3), (1, 2, 2), (1, 2, 3), (2, 2, 3), (1, 2, 2, 3)]







# 例如例子中的
[2,2,3] 与 【2，3，2】  可以归于同一个类别的内容。











