

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
示例 1:

输入: [1,2,3]
输出: 6

示例 2:

输入: [1,2,3,4]
输出: 24

# 下面的方法会超出内存的限制。
from typing import List
import itertools

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        list2 = list(itertools.combinations(nums, 3))
        list3 = []
        for i in list2:
            list3.append(i[0]*i[1]*i[2])

        temp = max(list3)
        return temp

# 方法二：
class Solution(object):
    def maximumProduct(self, nums):
        max_1, max_2, max_3 = -1001, -1001, -1001
        min_1, min_2 = 1001, 1001
        for i in range(len(nums)):
            if nums[i] > max_1:
				max_3 = max_2
                max_2 = max_1
                max_1 = nums[i]
            elif nums[i] > max_2:
                max_3 = max_2
                max_2 = nums[i]
            elif nums[i] > max_3:
                max_3 = nums[i]

            if nums[i] < min_1:
                min_2 = min_1
                 min_1 = nums[i]
            elif nums[i] < min_2:
                min_2 = nums[i]
        return max(min_1*min_2*max_1, max_3*max_2*max_1)



# 方法三
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

# 例如下面这种情况：
# 存在负数的情况的时候,
# [1, 12, -5, -6, 50, 3]
# 经过排序之后的数组为:
# [-6, -5, 1, 3, 12, 50]

# 所以最大的数字只能是(-6*(-5)*50  或者是(3*12*50))
# 两种情况中的一种情况.


if __name__ == '__main__':
    s = Solution()
    print(s.maximumProduct([1, 2, 3, 4]))
