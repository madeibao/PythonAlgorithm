

# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root: return []
        queue = deque()
        queue.appendleft(root)
        res = []
        while queue:
            tmp = []
            n = len(queue)
            for _ in range(n):
                node = queue.pop()
                tmp.append(node.val)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            res.insert(0, tmp)
        return res


if __name__ == "__main__":
	s =Solution()

	n2 = TreeNode(1)
	n3 = TreeNode(2)
	n4 = TreeNode(3)

	n2.left = n3	
	n2.right = n4

	print(s.levelOrderBottom(n2))

	