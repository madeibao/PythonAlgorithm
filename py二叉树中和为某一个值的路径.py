
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        if not root: return res
        def helper(root, list2, tempval):

            if not root: return res
            if (tempval==sum) and not root.left and not root.right:
                res.append(list2)

            if root.left:
                helper(root.left, list2+[root.val],tempval+root.val)
            if root.right:
                helper(root.right,list2+[root.val],tempval+root.val)

        helper(root, [root.val], root.val)

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