
# 给你一个整数数组 A 和一个整数 K，请在该数组中找出两个元素，使它们的和小于 K 但尽可能地接近 K，返回这两个元素的和。
# 如不存在这样的两个元素，请返回 -1。
# 输入：A = [34,23,1,24,75,33,54,8], K = 60
# 输出：58
# 解释：
# 34 和 24 相加得到 58，58 小于 60，满足题意。

#----------------------------------------------------------------------------------------

from typing import List


# class Solution:
#     def twoSumLessThanK(self, A: List[int], K: int):
#         res = -1
#         n = len(A)
#         for i in range(n):
#             for j in range(i+1, n):
#                 t = A[i] + A[j]
#                 if t < K:
#                     res = max(res, t)
        
#         return res

#----------------------------------------------------------------

class Solution():
    def twoSumLessThanK(self, A, K):
        A.sort()
        res = -1
        n = len(A)

        l=0
        r=n-1
        while l<r:
            t = A[l]+A[r]
            if t>= K:
                r-=1
            else:
                res = max(res, t)
                l+=1 
        return res




if  __name__ == "__main__":
    s = Solution()
    nums = [34,23,1,24,75,33,54,8]
    K = 60
    print(s.twoSumLessThanK(nums, K))


                