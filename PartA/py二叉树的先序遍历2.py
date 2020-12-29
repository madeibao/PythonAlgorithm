

# 二叉树的先序的遍历方法。


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)

            # 先添加的是右子树。
            if node.right:
                stack.append(node.right)

            # 后添加的是左子树。
            if node.left:
                stack.append(node.left)
        return res


if __name__ == "__main__":
    s = Solution()
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n2.left = n3
    n2.right = n4

    print(s.preorderTraversal(n2))






