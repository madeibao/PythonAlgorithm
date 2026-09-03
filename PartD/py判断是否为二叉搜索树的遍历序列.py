
# 二叉搜索树的后序的遍历序列。
# 
from typing import List, Tuple


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        
        def helper(nums):
            if len(nums) <= 1: return True
            root = nums[-1]

            # 找到一个节点，节点的值会大于根节点的位置值。
            for i in range(len(nums)):
                if nums[i] > root: break

            for j in range(i, len(nums)-1):
                if nums[j] < root: return False
            return helper(nums[:i]) and helper(nums[i:-1])
        
        if not postorder: return True
        return helper(postorder)



if __name__ == "__main__":
    s = Solution()
    nums = [1,3,2,6,5]
    print(s.verifyPostorder(nums))

