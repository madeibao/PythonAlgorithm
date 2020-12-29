

while True:
    try:
        from typing import List
        from functools import reduce
        class Solution:
            def singleNumber(self, nums: List[int]) -> int:
                return reduce(lambda x, y: x ^ y, nums)

        if __name__ == "__main__":
            s = Solution()
            num= int(input())
            nums= list(map(int, input().split(" ")))
            print(s.singleNumber(nums))

    except:
        break


