
from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return 0
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        # lambda 表达式的写法：
        key2 = cmp_to_key(lambda a, b: int(a+b)- int(b+a))
        nums.sort(key=cmp_to_key(compare))
        return "".join(nums).lstrip("0") or "0"


if __name__ == '__main__':
    nums = [10, 2]
    print(Solution.maxNum('', nums))