

# 递归来实现二叉树的后序遍历序列。
from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def helper(nums):
            if len(nums)<1: return True
            root = nums[-1]
            i = 0

            # 找到比根节点大的节点的位置值。
            for i_ in range(len(nums)-1):
                if nums[i_] > root: break
                i += 1

            # 对应位置的节点，一定都比根节点的值要大。
            for j in range(i, len(nums)-1):
                if nums[j] < root: return False
            return helper(nums[:i]) and helper(nums[i:-1])
        if not postorder: return True
        return helper(postorder)

if __name__ == '__main__':
    s = Solution()
    list2 = [1, 3, 2, 6, 5]
    print((s.verifyPostorder(list2)))





