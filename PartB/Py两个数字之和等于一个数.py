
# 对于给定的两个数字，求出等于某一个数字的和。


class Solution():
    def SumOfTwo(self,nums, target):
        dic = {}
        for key , value in enumerate(nums):
            if dic.get(target - value) is not None:
                return [key, dic.get(target - value)]
            dic[value] = key


if __name__ == "__main__":
    s =Solution()
    nums = [2, 7, 8, 9, 10]
    target = 9
    print(s.SumOfTwo(nums, target))













