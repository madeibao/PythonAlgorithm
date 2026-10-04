from typing import List


def getSum(num: int) -> int:
    res = 0
    while num:
        res += num % 10
        num = num // 10
    return res


class Solution:
    def minElement(self, nums: List[int]) -> int:

        res = []
        for i in nums:
            res.append(getSum(i))
        return min(res)


if __name__ == "__main__":
    nums = [10, 12, 13, 14]
    print(Solution().minElement(nums))
