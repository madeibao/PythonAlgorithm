# 前向后向的思想，先从左往右遍历，数组a[i]记录以i结尾的子数组的乘积，
# 再从右往左遍历，数组b[i]记录以i开始的子数组的乘积
# 那么对应于位置i的结果就是a[i-1]*b[i+1]


from typing import List
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1): # bottom triangle
            p *= nums[i]
            res.append(p)
        for i in range(len(nums) - 1, 0, -1): # top triangle
            q *= nums[i]
            res[i - 1] *= q
        return res

# 算法的精妙之处，双向遍历的算法。
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, m, n = [1] * len(nums), 1, 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i], m = res[i] * m, m * nums[i]
            res[j], n = res[j] * n, n * nums[j]
        return res

#python的前缀积和后缀积来计算得出最终的结果值。
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

# 下面的算法会超时。
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list2 = []
        list3 = []

        for i in nums:
            temp =[]
            temp.extend(nums)
            temp.remove(i)
            list2.append(temp)

        def getnum(num2):
            mul = 1
            for i in num2:
                mul *= i
            return mul
        for j in list2:
            list3.append(getnum(j))
        return list3



if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))






