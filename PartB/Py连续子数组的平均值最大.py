# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

# 示例 1:

# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi=sum(nums[:k])
        temp=maxi
        for i in range(len(nums)-k):
            temp=temp-nums[i]+nums[i+k] 
            #不要不断的用 sum 进行计算sum(nums[i:i+k]),这样耗时
            maxi=max(maxi,temp)
        return maxi/float(k)


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3], 4))