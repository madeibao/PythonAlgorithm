
# 数字的内容来重新的进行排序，使得，组合成为最大的数字内容。

from typing import List

class Solution():
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        def helper(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
    
        #  去除左面的0,如果有0则需要去除0.

        return "".join(sorted(map(str, nums), key=cmp_to_key(helper))).lstrip("0") or "0"

    
if __name__ == "__main__":
    s= Solution()
    list2 = [1,2,0,3,45]
    print(s.largestNumber(list2))

#----------------------------------------------------------------
'''
class Solution():
    def largestNumber(self, nums: List[int]) -> str:
        class large_num(str):
            def __lt__(self, other):
                return self + other > other + self
        return "".join(sorted(map(str, nums), key=large_num)).lstrip("0") or "0"

'''


