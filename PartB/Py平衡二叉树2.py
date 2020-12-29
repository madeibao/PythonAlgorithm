
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left=None
        self.right= None



class Solution():
	def palindrome(self,root):

		if not root:
			return True
		return valid(root.left, root.right)

		def valid(L, R):
			if not L and not R:
				return True

			if not L or not R:
				return False 


			# 按照顺序来执行的结果值。
			if L.val!=R.val:
				return False

			return valid(L.left, R.right) and valid(L.right, R.left)


if __name__=='__main__':
	s = Solution()

	n2 = TreeNode(1)
	n3 = TreeNode(2)
	n4 = TreeNode(2)

	n2.left =n3	
	n2.right = n4

	print(s.palindrome(n2))

