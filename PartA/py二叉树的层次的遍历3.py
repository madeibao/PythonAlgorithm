

from collections import deque	


class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def levelTree(self,root):

		if not root:
			return []
		queue2 = deque()
		queue2.append(root)

		res = []
		while queue2:
			for i in range(len(queue2)):
				temp = queue2.popleft()
				res.append(temp.val)
				if temp.left!=None:
					queue2.append(temp.left)
				if temp.right!=None:
					queue2.append(temp.right)
		return res


if __name__ == "__main__":
	s = Solution()

	n2 =TreeNode(2)
	n3 =TreeNode(3)
	n4 =TreeNode(4)

	n2.left = n3
	n2.right = n4

	res = s.levelTree(n2)
	print(res)



