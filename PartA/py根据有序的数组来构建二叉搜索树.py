

# Definition for a binary tree node.
from typing import List


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(nums) - 1)


# 中序遍历序列，得到的是有序的数组。
def helper(root):
    if not root:
        return []
    res = []
    helper(root.left)
    print(root.val, end=" ")
    helper(root.right)
    return res


if __name__ == '__main__':
    s = Solution()
    list2 = [1, 2, 3, 4, 5, 6, 7]
    res = s.sortedArrayToBST(list2)
    helper(res)
