


题目描述
依次给出n个正整数A1，A2，… ，An，将这n个数分割成m段，每一段内的所有数的和记为这一段的权重， m段权重的最大值记为本次分割的权重。问所有分割方案中分割权重的最小值是多少？
输入描述:
第一行依次给出正整数n，m，单空格切分；(n <= 10000, m <= 10000, m <= n)
第二行依次给出n个正整数单空格切分A1，A2，… ，An  (Ai <= 10000)
输出描述:
分割权重的最小值
示例1
输入
复制
5 3
1 4 2 3 5
输出
复制
5
说明
分割成 1  4 |   2   3  |   5  的时候，3段的权重都是5，得到分割权重的最小值。


#------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------


from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        def helper(mid):
            cur = 0
            res = 1
            for num in nums:
                cur += num 
                if cur > mid:
                    res += 1
                    cur = num 
            return res 
        
        while left < right:
            mid = (left + right) // 2
            if helper(mid) > m:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    s =Solution()
    a, b = map(int, input().split(" "))

    list2 = list(map(int, input().split( )))
    print(s.splitArray(list2, b))

