

# 列表中的元素内容来组成最小的数字。


from functools import cmp_to_key


class Solution(object):
    def minNum(self, nums):
        if not nums:
            return 0
        list2 = list(map(str, nums))
        keys = cmp_to_key(lambda a, b: int(a + b) - int(b + a))
        return "".join(sorted(list2, key=keys)).lstrip("0")

if __name__ == "__main__":
    
    s = Solution()
    list2 = [1, 3, 2, 49, 12]
    print(s.minNum(list2))




