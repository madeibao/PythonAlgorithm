

# # 一个数字的左面和右面都比他小，则为峰值
# 峰值元素是指其值大于左右相邻值的元素。
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
# 你可以假设 nums[-1] = nums[n] = -∞。
# 示例 1:
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:

# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5 
# 解释: 你的函数可以返回索引 1，其峰值元素为2;
#      或者返回索引 5， 其峰值元素为 6。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-peak-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# ================================================================================
#========================================================================
#========================================================================


from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))

class Solution():
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2    # 这种写法比 (left+right)//2 求mid的方法好，一些语言这样写可以防止溢出
            if nums[mid] > nums[mid + 1]:       # 如果满足该条件说明山峰可能是在 mid 的左侧，因为各个元素不同，所以if的条件是 >
                right = mid
            else:
                left = mid + 1
        return left

#================================

if __name__ == "__main__":
    list2 = [1,2,3,1]
    s2 = Solution()
    print(s2.findPeakElement(list2))


        