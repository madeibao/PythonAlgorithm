



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left=None
        self.right= None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def help(root:TreeNode, i:int) -> int:
            if not root:
                return 0
            res  = i*10 + root.val  
            if root.left==None and root.right==None:
                return res
            return help(root.left, res) + help(root.right,res)

        return help(root, 0)


if __name__ == "__main__":
	s = Solution()
	n2 = TreeNode(1)
	n3 = TreeNode(2)
	n4 = TreeNode(3)

	n2.left = n3
	n2.right = n4

	print(s.sumNumbers(n2))






