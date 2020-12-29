


from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        if not nums:
            return ''
        nums = map(str, nums)
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        # lstrip() 方法: 截掉字符串左边的空格或指定字符  0012->12
        res = ''.join(sorted(nums, key=key)).lstrip('0')
        # 000->''
        return res or '0'



if __name__ == '__main__':
    s = Solution()
    list2 = [10, 2]
    print(s.largestNumber(list2))

