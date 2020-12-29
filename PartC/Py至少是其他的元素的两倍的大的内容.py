在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
如果是，则返回最大元素的索引，否则返回-1。

示例 1:

输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.





from typing import List


# 本人的解法:

# 输入: nums = [3, 6, 1, 0]
# 输出: 1
# 解释: 6是最大的整数, 对于数组中的其他整数,
# 6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.

from typing import List


class Solution():
    def dominantIndex(self, nums: List[int]) -> int:
        num2 = max(nums)
        temp = 0
        for i in nums:
            if i == num2:
                continue
            elif num2 < i*2:
                temp = -1
                break
            else:
                temp = nums.index(num2)
        return temp


if __name__ == '__main__':
    s = Solution()
    print(s.dominantIndex([3, 6, 1, 0]))



#================================================================


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        r = max(nums)
        index = 0
        for i in range(len(nums)):
            if r != nums[i] and r < 2 * nums[i]:
                return -1
            if r == nums[i]:
                index = i
        return index


if __name__ == '__main__':
    s = Solution()
    print(s.dominantIndex([1, 2, 5, 4, 2]))