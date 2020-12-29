

class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        sump = nums[0]
        max_t = nums[0]
        for p in nums[1:]:
            sump = max(sump+p, p)
            max_t = max(sump, max_t)

        return max_t

    def DC(self, nums):
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0], nums[0], nums[0], nums[0]
        if len_nums == 2:
            sum_all = nums[1] + nums[0]
            max_tail = max(nums[1], sum_all)
            max_head = max(nums[0], sum_all)
            max_all = max(max_tail, nums[0])
            return max_head, max_tail, max_all, sum_all
        max_head_l, max_tail_l, max_all_l, sum_all_l = self.DC(nums[:len_nums//2])
        max_head_r, max_tail_r, max_all_r, sum_all_r = self.DC(nums[:len_nums // 2-1:-1])

        return max(max_head_l, sum_all_l+max_tail_r),\
               max(max_head_r, sum_all_r+max_tail_l),\
               max(max_all_l, max_all_r, max_tail_r+max_tail_l),\
               sum_all_l+sum_all_r

    def maxSubArray(self, nums: List[int]) -> int:

        return self.DC(nums)[2]


if __name__ == "__main__":
	s = Solution()
	list2 =  [-2,1,-3,4,-1,2,1,-5,4]
	print(s.maxSubArray(list2))



# ------------------------------------------------------------------------------------------------------------
from typing import List


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        sump = nums[0]
        max_t = nums[0]
        for p in nums[1:]:
            sump = max(sump + p, p)
            max_t = max(sump, max_t)
        return max_t


if __name__ == "__main__":
    s = Solution()
    list2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray1(list2))









