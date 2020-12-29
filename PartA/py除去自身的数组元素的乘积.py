

给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/product-of-array-except-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
算法的精髓


# ----------------------------------------------------------------------------------------

from typing import List

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res, p, q = [1], 1, 1

        # 下三角的内容。
        for i in range(len(nums) - 1): # bottom triangle
            p *= nums[i]
            res.append(p)
        

        # 上三角的内容。
        for i in range(len(nums) - 1, 0, -1): # top triangle
            q *= nums[i]
           	# 从后面向前面来相乘。
            res[i - 1] *= q
        return res


if __name__ == "__main__":
	s = Solution()

	list2 = [1,2,3,4,5]
	res = s.productExceptSelf(list2)
	print(res)

