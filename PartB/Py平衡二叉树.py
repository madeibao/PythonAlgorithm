

class TreeNode(object):
	def __init__(self,x):
		self.val =  x
		self.left =None
		self.right =None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        if root.left==None and root.right==None:
            return True
        return abs(self.height(root.left)-self.height(root.right))<2  and self.isBalanced(root.left) and self.isBalanced(root.right)


	def height(self,head):
		if head==None:
			return 0
		if head.left==None and head.right==None: 
			return 1

		return max(height(head.left),height(head.right)) +1



if __name__=='__main__':
	s = Solution()
	n2 = TreeNode(1)
	n3 = TreeNode(2)
	n4 = TreeNode(3)

	n2.left = n3
	n2.right = n4

	print(s.balace(n2))


