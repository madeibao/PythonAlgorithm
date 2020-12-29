
# from typing import List

# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution():
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if(not nums or n<3):
            return None
        # 首先来进行排序。
        nums.sort()

        # 极大值。
        res=float("inf")
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                cur_sum=nums[i]+nums[L]+nums[R]
                
                if(cur_sum==target):
                    return target
                if(abs(cur_sum-target)<abs(res-target)):
                    res=cur_sum
                if(cur_sum-target<0):
                    L+=1
                else:
                    R-=1
        return res  # 返回最终的结果值。


if __name__=='__main__':
    s = Solution()
    print(s.threeSumClosest([-1,1,2,-4], 1))

