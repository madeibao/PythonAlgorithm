 

# 一个数组中的滑动窗口的最大值。


class Solution(object):
    def maxWindow(self,nums, k):
        res = []
        for i in range(0, len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    s = Solution()
    print(s.maxWindow(nums, k))




