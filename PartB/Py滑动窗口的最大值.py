给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。

你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。
返回滑动窗口最大值。


示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

[3,3,5,5,6,7] 

解释: 
# 暴力破解法，求滑动窗口的最大值。
class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:return []
        l = []
        for i in range(len(nums) - k + 1):
            l.append(max(nums[i:i+k]))
        return l


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        window, res = [], []   # res保留最终的结果值。/
        for i, n in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= n:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))




给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subarray-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。