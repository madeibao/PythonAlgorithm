

# 二叉树的右视图，从右面观察自上而下得到的数字。


from typing import List
import collections


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        d = collections.deque()
        d.append(root)
        res = []
        while d:
            n = len(d)
            for i in range(n):
                node = d.popleft()
                if i == n-1:
                    res.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return res


if __name__ == "__main__":
	s =Solution()
	n2 =TreeNode(2)
	n3 =TreeNode(3)
	n4 =TreeNode(4)

	n2.left = n3
	n2.right = n4

	print(s.rightSideView(n2))

