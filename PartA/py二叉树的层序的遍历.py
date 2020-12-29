

# 二叉树的锯齿形的遍历值。
class TreeNode(object):
	def __init__(self, x):
		self.left = None
		self.right = None
		self.val = x


from typing import List, Tuple
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        curr = [root]
        res = []
        while curr:
            temp = []
            n = len(curr)
            for i in range(n):
                node = curr.pop(0)
                temp.append(node.val)
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            res.append(temp)
        # res的临时的结果值，对特殊的层来进行逆置。
        # 如果是奇数的层次。
        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()
        return res


if __name__  == "__main__":
	s = Solution()
    s = Solution()

    root = TreeNode(2)
    n2 = TreeNode(9)
    n3 = TreeNode(20)

    n4 = TreeNode(15)
    n5 = TreeNode(7)

    root.left = n2
    root.right = n3

    n3.left = n4
    n3.right = n5

    res = s.zigzagLevelOrder(root)
    print(res)

