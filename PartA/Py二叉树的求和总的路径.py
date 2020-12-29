
class TreeNode(object):
	def __init__(self,x):
		self.val =  x
		self.left =None
		self.right =None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
    	if not root:
    		return 0
    	return self.path(root,sum)+self.path(root.left,sum)+self.path(root.right,sum)

    def path(self, root, sum):
    	if not root:
    		return 0
    	res =0
    	if root.val ==sum:
    		res+=1
    	res+= self.path(root.left,sum-root.val)
    	res+= self.path(root.right,sum-root.val)

    	return res 

if __name__ == "__main__":

	
	s = Solution()
	root = TreeNode(5)

	n2 = TreeNode(4)
	n3 = TreeNode(8)

	n4 = TreeNode(11)
	n5 = TreeNode(13)
	n6 = TreeNode(4)

	n7 = TreeNode(7)
	n8 = TreeNode(2)
	n9 = TreeNode(5)
	nA = TreeNode(1)

	root.left = n2
	root.right = n3

	n2.left = n4

	n3.left = n5
	n3.right = n6

	n4.left = n7
	n4.right = n8

	n6.left = n9
	n6.right = nA

	print(s.pathSum(root,22))






