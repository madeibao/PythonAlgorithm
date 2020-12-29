

from typing import List, Tuple


class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None 
		self.right = None


class Solution():
	def averageOfLevels(self,root:TreeNode) -> List[float]:
		if not root:return []

		temp = root
		queue = [root]
		res = []

		while queue:
			temp = []
			for _ in range(len(queue)):
				node = queue.pop(0)
				if node:
					temp.append(node.val)
					queue.append(node.left)
					queue.append(node.right)
			l = len(temp)
			if l>0:
				aver = sum(temp)/l
				res.append(aver)
		return res 

if __name__ == "__main__":
	s = Solution()

	root = TreeNode(3)
	n2 = TreeNode(9)
	n3 = TreeNode(20)

	n4 = TreeNode(15)
	n5 = TreeNode(7)

	root.left = n2
	root.right = n3 

	n3.left = n4
	n3.right = n5 

	res = s.averageOfLevels(root)
	print(res)






	