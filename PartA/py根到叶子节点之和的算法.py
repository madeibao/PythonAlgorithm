

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None 
		self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def help(root: TreeNode, i: int) -> int:
            if not root:
                return 0
            temp = i * 10 + root.val
            if root.left == None and root.right == None:
                return temp

            return help(root.left, temp) + help(root.right, temp)

        return help(root, 0)


if __name__ == "__main__":
	s = Solution()
	root = TreeNode(1)
	n2 =TreeNode(2)
	n3 = TreeNode(3)

	root.left = n2
	root.right = n3

	print(s.sumNumbers(root))