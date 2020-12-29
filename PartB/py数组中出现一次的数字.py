


# 数组中的有的数字只出现了一次，找出这些数字。
# http://www.baidu.com


from collections import Counter

class Solution():
    def fun(self,nums):
        count = Counter(nums)
        return [x for x in count if count[x]==1]


if __name__ == "__main__":

    s = Solution()
    list2 = [1,2,1,3,2,5]
    print(s.fun(list2))




