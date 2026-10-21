from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        f_max = f_min = 1
        for x in nums:
            if x < 0:
                # 下面与 x 相乘后，最大的正数变成最小的负数，最小的负数变成最大的正数
                # 提前交换，这样可以把 x < 0 和 x >= 0 的情况合并，合并后，计算 max 和 min 可以少一项
                f_max, f_min = f_min, f_max
            f_max = max(f_max * x, x)
            f_min = min(f_min * x, x)
            ans = max(ans, f_max)
        return ans
        

class Solution2:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A),max(B)) 


if __name__ == "__main__":
    nums = [2,3,-2,4]
    print(Solution().maxProduct(nums))
    print(Solution2().maxProduct(nums))


# 代码求的是最大的乘积子数组，而不是连续子数组，所以不能用滑动窗口来做
