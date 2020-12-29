

# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:

# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]

#----------------------------------------------------------------
#----------------------------------------------------------------

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def move(nums, i, j):
        	while i<j:
        		nums[i],nums[j] = nums[j], nums[i]
        		i+=1
        		j-=1

        n = len(nums)
        k = k % len(nums)

        move(nums, 0, n-k-1)
        move(nums, n-k, n-1)
        move(nums, 0, n-1)
        return nums


if __name__ == "__main__":
	s = Solution()
	list2 = [1, 2, 3,4,5,6,7]
	k =3
	print(s.rotate(list2, k))

