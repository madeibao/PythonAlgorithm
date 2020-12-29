


from functools import cmp_to_key

class Solution():
    def minnum(self, nums):

        if not nums:
            return ""
        

        # 首先来映射成为字符串数组。

        nums = map(str, nums)
        key = cmp_to_key(lambda x,y:int(y+x)-int(x+y))

        # 去除前置的字符0
        nums = "".join(sorted(nums, key=key)).lstrip("0")
        return nums or "0"

if __name__ == "__main__":
    s =Solution()
    list2 =[10,2]
    print(s.minnum(list2))


