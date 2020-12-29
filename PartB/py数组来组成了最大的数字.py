

# 数组来组成最大的数字。



from functools import cmp_to_key
from typing import List


class Solution():
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        nums = map(str, nums)
        key2 = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        res = "".join(sorted(nums, key=key2)).lstrip('0')
        return res or "0"


if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([1, 2, 2, 3]))
