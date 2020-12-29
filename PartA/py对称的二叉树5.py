

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def symmetric(self,root):
		def helper(left, right):

			# 必须是首先判断两个树是否都为空树，然后再判断其中的一个是否为空树。
			if not left and not right:
				return True
			if not left or not right:
				return False
			return left.val==right.val and helper(left.left,right.right) and helper(left.right,right.left)
		return helper(root.left,root.right)


if __name__ == "__main__":
	s =Solution()
	n2 =TreeNode(1)
	n3 =TreeNode(2)
	n4 =TreeNode(2)

	n2.left = n3
	n2.right = n4
	print(s.symmetric(n2))








