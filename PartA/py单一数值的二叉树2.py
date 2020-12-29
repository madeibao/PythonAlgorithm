


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            val = root.val
            if root.left and root.left.val != val:
                return False
            elif root.right and root.right.val != val:
                return False
            else:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
'''

class Solution():
	def isUnivalTree(self, root):

		stack = []

		stack.append(root)
		val = root.val
		while stack:
			temp = stack.pop()
			if temp and temp.val!=val:
				return False
			elif temp:
				stack.append(temp.left)
				stack.append(temp.right)
		return True

if __name__ == "__main__":
	s =Solution()
	n2 = TreeNode(1)
	n3 = TreeNode(1)
	n4 = TreeNode(1)

	n2.left = n3	
	n2.right = n4

	print(s.isUnivalTree(n2))