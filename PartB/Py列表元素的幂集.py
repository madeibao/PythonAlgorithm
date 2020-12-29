

from typing import List

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        幂集
        也就是生成集合的所有子集
        设 p(n) 表示 n 个元素的所有子集，那么有
        p(0) = {}
        p(1) = {}, {n1}
        p(2) = {}, {n1}, {n2}, {n1, n2}
        p(3) = {}, {n1}, {n2}, {n1, n2}, {n3}, {n1, n3}, {n2, n3}, {n1, n2, n3}
        注意到 p(3) = p(2) + (n3 和每个 p(2) 元素的组合)
        依次类推，我们就可以得到 p(n) 的计算方案，实际上就是在上层集合上不断的累计。
        """
        res = [[]]
        for n in nums:
            res += [sub + [n] for sub in res]
        return res
'''

# 回溯算法。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, tmp, start):
            res.append(tmp[:])
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                backtrack(nums, tmp, i+1)
                tmp.pop()
            
        backtrack(nums, [], 0)
        return res





if __name__ == "__main__":
	s =Solution()
	list2 = [1,2,3]
	print(s.subsets(list2))


# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]





