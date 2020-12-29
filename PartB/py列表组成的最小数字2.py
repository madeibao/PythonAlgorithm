




from functools import cmp_to_key


class Solution(object):
    def minnum(self, nums):
        str2 = list(map(str, nums))
        cmp2 = cmp_to_key(lambda a, b: int(a + b) - int(b + a))
        return "".join(sorted(str2, key=cmp2)).lstrip("0")

if __name__ == "__main__":
    s = Solution()
    list2 = [10, 2]
    print(s.minnum(list2))


