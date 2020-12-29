
输入：arr = [15,13,12]
输出：14
解释：原来的数组是 [15,14,13,12]。


class Solution:
    def missingNumber(self, A: List[int]) -> int:
        return (A[0] + A[-1]) * (len(A) + 1) // 2 - sum(A)

if __name__ == "__main__":
    s = Solution()
    arr = [15,13,12]
    print(s.missingNumber(arr))