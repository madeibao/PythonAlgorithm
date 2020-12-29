

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        list2 = []
        for i in range(2 ** N):  # 子集的个数
            combo = []
            for j in range(N):   # 用来判断二进制数的下标为j的位置的数是否为1
                if (i >> j) % 2:
                    combo.append(nums[j])
            list2.append(combo)
        return list2


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 3 ]))



# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]



