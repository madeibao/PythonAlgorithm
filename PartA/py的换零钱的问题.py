

常见的背包问题有1、组合问题。2、True、False问题。3、最大最小问题。
以下题目整理来自大神CyC，github地址：
github
我在大神整理的基础上，又做了细分的整理。分为三类。


1、组合问题：
通用的公式:

dp[i] += dp[i-num]

377. 组合总和 Ⅳ
494. 目标和
518. 零钱兑换 II



2、True、False问题：

通过的公式：

139. 单词拆分
416. 分割等和子集


3、最大最小问题：
474. 一和零
322. 零钱兑换




leetcode 377 问题:
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                dp[i] += dp[i - num]
        return dp[target]

if __name__ == "__main__":
	s =Solution()
	nums = [1,2,3]
	target = 4

	s = Solution()
	print(s.combinationSum4(nums, target))

#------------------------------------------------------------------------------------------------

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

 

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

                  sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                       2 * sum(P) = target + sum(nums)

class Solution():
    def findTargetSum(self, nums, S):
        def subSetSum(nums, s):
            dp = [0 for _ in range(s + 1)]

            dp[0] = 1
            for i in nums:
                for j in range(s, i - 1, -1):
                    dp[j] += dp[j - i]
            return dp[s]


        sum2 = 0
        for i in nums:
            sum2 += i
        if sum2 < S or (S + sum2) % 2 > 0:
            return 0
        else:
            return subSetSum(nums, (S + sum2) // 2)


if __name__ == "__main__":
    s = Solution()
    list2 = [1, 1, 1, 1, 1]
    S = 3
    print(s.findTargetSum(list2, S))


#-----------------------------------------------------------------------------------
零钱兑换算法：

给定金额与硬币的，硬币数量无限制。
求一共由多少种方法

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0 for _ in range(amount)]

        # for i in range(1, len(coins)+1):
        #     for j in range(coins[i-1], amount+1):
        #         dp[j] = dp[j] + dp[j-coins[i-1]]

        for w in coins:
            for j in range(w, amount+1):
                dp[j] += dp[j-w]

        # for w in coins:
        #     for j in range(amount - w + 1):
        #         if dp[j]:
        #             dp[j + w] += dp[j]


        # 返回最后的一个就是结果值。
        return dp[-1] 


if __name__ == "__main__":
	s = Solution()
	list2 = [1,2,5]
	amount =5 
	print(s.change(list2, amount))

