
# 二叉树的右视图，

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

from collections import deque

class Solution(object):
	def rightview(self, root):

		res = []
		queue = deque()
		if not root:return res
		queue.append(root)

		while queue:
			n = len(queue)
			for  i in range(n):
				node = queue.popleft()
				if i==n-1:
					res.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
		return res

if __name__ == '__main__': 
	s = Solution()
	n2 = TreeNode(1)
	n3 = TreeNode(2)
	n4 = TreeNode(3)

	n2.left = n3
	n2.right = n4

	res =s.rightview(n2)
	print(res)





