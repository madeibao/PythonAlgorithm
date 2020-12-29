

输入：A = [34,23,1,24,75,33,54,8], K = 60
输出：58
解释：
34 和 24 相加得到 58，58 小于 60，满足题意。
#----------------------------------------------------------------------------------------


from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        n = len(A)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                temp = A[i] + A[j]
                if temp < K:
                    res = max(res, temp)
        return res


if __name__ == "__main__":
    s = Solution()
    A = [34,23,1,24,75,33,54,8]
    K = 60
    print(s.twoSumLessThanK(A, K))

