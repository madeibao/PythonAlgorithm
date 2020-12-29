# # 算法思想；
# 下面介绍动态规划的做法，复杂度为 O(n)。
# 　　步骤 1：令状态 dp[i] 表示以 A[i] 作为末尾的连续序列的最大和（这里是说 A[i] 必须作为连续序列的末尾）。
# 　　步骤 2：做如下考虑：因为 dp[i] 要求是必须以 A[i] 结尾的连续序列，那么只有两种情况：
#  这个最大和的连续序列只有一个元素，即以 A[i] 开始，以 A[i] 结尾。
#  这个最大和的连续序列有多个元素，即从前面某处 A[p] 开始 (p<i)，一直到 A[i] 结尾。
# 　　对第一种情况，最大和就是 A[i] 本身。
# 　　对第二种情况，最大和是 dp[i-1]+A[i]。
# 　　于是得到状态转移方程：
# 　　　　　　　　dp[i] = max{A[i], dp[i-1]+A[i]}
# 　　这个式子只和 i 与 i 之前的元素有关，且边界为 dp[0] = A[0]，由此从小到大枚举 i，即可得到整个 dp 数组。
#   接着输出 dp[0]，dp[1]，...，dp[n-1] 中的最大子即为最大连续子序列的和。



def method1(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
    return max(nums)


print(method1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# 这种可以针对有负数的情况来进行判断。



class Solution(object):
    def maxSubArray(self, nums):
        sum2 = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum2 += num
            if sum2 > max_sub_sum:
                max_sub_sum = sum2
            if sum2 < 0:
                sum2 = 0
        return max_sub_sum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#----------------------------------------------------------------
# 动态规划的思想来进行判断，从而决定着所有的和。


class Solution():
    def getnum(self, nums):
        list2 = [0 for i in range(len(nums))]   # 首先进行初始化的操作。
        list2[0] = nums[0]
        ans = list2[0]
        for i in range(len(nums)):
            list2[i] = max(nums[i]+list2[i-1], nums[i])
            if list2[i] > ans:
                ans = list2[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getnum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



# 最大的联系子数组的和，变体模型

# 如果联系的子数组的和为负值，则令其为0

while True:
    try:
        class Solution(object):
            def maxSubArray(self, nums):
                sum2 = 0
                max_sub_sum = nums[0]
                for num in nums:
                    sum2 += num
                    if sum2 > max_sub_sum:
                        max_sub_sum = sum2
                    if sum2 < 0:
                        sum2 = 0
                if max_sub_sum < 0:
                    max_sub_sum = 0
                return max_sub_sum

        if __name__ == '__main__':
            s = Solution()
            list1 = list(map(int, input().split(",")))
            print(s.maxSubArray(list1))
    except:
        break
