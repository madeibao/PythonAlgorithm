
from typing import List
import collections


class Solution:
    def findSumEqual(self, N, L):
        Inf = 1000000000
        if N > Inf:
            return False
        mid = N // 2 - 1
        res= []
        nums = list(range(1, mid + 1))
        i, j = mid - L - 1, mid + 1
        while i >= 0 and j >= L - 1:
            total = sum(nums[i: j])
            if total > N:
                j -= 1
            elif total < N:
                i -= 1
            else:
                for x in nums[i: j]:
                    res.append(x)
                break
        if len(res)!= 0:
            return res
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.findSumEqual(65, 4))
