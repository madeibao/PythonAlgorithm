
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrder(root):
    if not root:
        return
    print(root.val, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 实际上inorder 和 postorder一定是同时为空的，因此你无论判断哪个都行
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i+1:])

        return root


if __name__ == "__main__":
	s =Solution()
	pre = [3,9,20,15,7]
	inorder = [9,3,15,20,7]
	res = s.buildTree(pre,inorder)
	preOrder(res)

