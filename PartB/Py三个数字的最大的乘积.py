

#一个数组中的三个数字的最大的乘积， 可能包含有负数
#================================================================
#================================================================


from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

               

if __name__ == "__main__":
    s = Solution()
    print(s.maximumProduct([1,2,3,4,5,6]))




