

from collections import deque	


class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def traversal(self,root):
		if not root:
			return []
		res = []

		queue2 = deque()
		while queue2:
			temp = []
			n = len(queue2)
			for i in range(n):
				node = queue2.popleft()
				temp.append(node.val)
				if node.left:
					queue2.append(node.left)
				if node.right:
					queue2.append(node.right)
			res.append(temp)

		return res

if __name__ == "__main__":
	s = Solution()

	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(4)

	n2.left = n3
	n2.right = n4

	print(s.traversal(n2))
