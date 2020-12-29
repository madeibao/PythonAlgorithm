

# 列表的全排列的实现。
# 全排列算法

class Solution(object):
    def permutations(self, nums):

        if nums is None:
            return []
        res = []

        def helper(start):
            if start == len(nums):
                res.append(nums[:])

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                helper(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        helper(0)
        return res


if __name__ == "__main__":
    s = Solution()
    list2 = [1, 2, 3]
    print(s.permutations(list2))



# 组合算法的实现


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        N = len(nums)

        def helper(idx, temp_list):
            res.append(temp_list)
            for i in range(idx, N):
                helper(i + 1, temp_list + [nums[i]])

        helper(0, [])
        return res


if __name__ == "__main__":
    s = Solution()
    list2 = [1, 2, 3,]
    print(s.subsets(list2))


