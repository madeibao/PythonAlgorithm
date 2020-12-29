



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left=None
        self.right= None



class Solution(object):
	def levelTree(self,root):

		if not root:
			return []
		res = []
		curList = [root]

		depth = 0

		while curList:

			temp =[]	
			nextLevel = []
			for node in curList:
				temp.append(node.val)
				if node.left:
					nextLevel.append(node.left)
				if node.right:
					nextLevel.append(node.right)

			if depth%2==0:
				res.append(temp[::-1])
			else:
				res.append(temp)
			depth+=1

			curList = nextLevel

		return res


if __name__ == "__main__":
	s = Solution()

	n2 = TreeNode(1)
	n3 = TreeNode(2)
	n4 = TreeNode(3)

	n2.left = n3
	n2.right = n4

	res = s.levelTree(n2)

	print(res)