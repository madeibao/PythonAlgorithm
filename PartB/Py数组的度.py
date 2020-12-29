给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释: 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

#================================================================================================



class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]] = [i]
            else:
                a[nums[i]].append(i)
        m = 0
        for i in a:
            m = max(m, len(a[i]))
        r = len(nums)
        for i in a:
            if len(a[i]) == m:
                r = min(r, a[i][-1] - a[i][0] + 1)
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.findShortestSubArray([1, 2, 2, 3, 1]))

