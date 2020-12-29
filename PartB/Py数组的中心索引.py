给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。

我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

示例 1:

输入: 
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释: 
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。


示例 2:

输入: 
nums = [1, 2, 3]
输出: -1
解释: 
数组中不存在满足此条件的中心索引。


# 下面的自己的方法会超时

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        temp = -1
        for i in range(len(nums)):
            list2 = nums[:i]
            list3 = nums[i+1:]
            if sum(list2) == sum(list3):
                temp = i
                break
        return temp

        
#别人的解法
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
		a=sum(nums[:0])
		b=sum(nums[1:])
		for i in range(0,len(nums)-1):
		    if a==b:
		        return i
		    a+=nums[i]
		    b-=nums[i+1]
		if a==b:
		    return len(nums)-1
		return -1



if __name__ == '__main__':
    s = Solution()
    print(s.pivotIndex([-1,-1,-1,0,1,1]))