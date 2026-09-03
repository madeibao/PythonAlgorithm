
class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

from collections import deque
from typing import List


class Solution(object):
	def rightSideView(self, root: TreeNode) -> List[int]:

		queue= deque()
		res = []

		if not root:
			return res
		queue.append(root)
		while queue:
			n = len(queue)
			for i in range(n):
				node = queue.popleft()
				if i==n-1:
					res.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
		return res

if __name__ == "__main__":
	s=  Solution()

	root = TreeNode(1)
	n2 = TreeNode(2)
	n3 = TreeNode(3)

	root.left = n2
	root.right = n3

	res = s.rightSideView(root)

	print(res)

