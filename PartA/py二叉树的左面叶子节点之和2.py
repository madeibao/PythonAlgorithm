

# 二叉树的左面的叶子节点的和。


class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution(object):
	def getLeft(self,root):

		if not root:
			return 0
		if not root.left and root.right:
			return root.val

		left2, sum2 = 0, 0

		if root.left!=None and root.left.left!=None and root.left.right==None:
			left2 = root.left.val
		else:
			sum2 = self.getLeft(root.left)
		right2 = self.getLeft(root.right)

		return left2+sum2 + right2


if __name__ == "__main__":
	s = Solution()

	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(4)

	n2.left = n3
	n2.right = n4
	print(s.getLeft(n2))


