
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

#========================================================================================


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()             # 首先进行排序。
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break                    # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue    # 2. skip the same 'nums[k]'.  结束当前的循环。
            i, j = k + 1, len(nums) - 1

            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))




   