# 输入: [3,30,34,5,9]
# 输出: 9534330


from typing import List

# from functools import cmp_to_key
# class Solution():
#     def largestNumber(self, nums: List[int]) -> str:
#         if not nums:
#             return ""
        
#         # 变成字符串的列表内容。
#         nums = list(map(str, nums))
#         nums.sort(key=cmp_to_key(lambda x, y: int(y+x) - int(x+y)))
#         return '0' if nums[0] == '0' else "".join(nums)


#-----------------------------------------------------------------------------


# 下面的是比较运算符的方法的重写内容。
class compare(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution():
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        nums = sorted(list(map(str, nums)), key=compare)
        return '0' if nums[0] == '0' else "".join(nums)



if __name__ == "__main__":
    s = Solution()
    list2 = [10, 2]
    print(s.largestNumber(list2))


#-----------------------------------------------------------------------------


