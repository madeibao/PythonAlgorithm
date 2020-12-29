
from collections import deque

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left= None
		self.right= None
class Solution(object):
	def levelTree(self,root):

		queue2 = deque()
		queue2.append(root)
		res = []
		while queue2:
			temp = []
			for _ in range(len(queue2)):
				node = queue2.popleft()
				temp.append(node.val)
				if node.left!=None:
					queue2.append(node.left)
				if node.right!=None:
					queue2.append(node.right)
			res.append(temp)

		for i in range(len(res)):
			if i%2==0:
				res[i] = res[i][::-1]
		return res

if __name__ == "__main__":
    s = Solution()
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n2.left = n3
    n2.right = n4
    print(s.levelTree(n2))


