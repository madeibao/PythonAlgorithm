
class TreeNode():
	def __init__(self, x):
		self.left = None
		self.right = None
		self.val = x


class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		if not root:
			return None

		root.left, root.right = root.right, root.left

		self.invertTree(root.left)
		self.invertTree(root.right)

		return root


def preOrder(root):
	if not root:
		return None

	print(root.val)
	preOrder(root.left)
	preOrder(root.right)


if __name__ == "__main__":
	s = Solution()

	n2 = TreeNode(4)
	n3 = TreeNode(2)
	n4 = TreeNode(7)

	n2.left = n3
	n2.right = n4

	res = s.invertTree(n2)
	preOrder(res)




