

from typing import List


class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def lowestCommonAncestor(self,root, p,q)->TreeNode:
		if root.val<p.val and root.val>q.val:
			return self.lowestCommonAncestor(root.right, p,q)

		if root.val>p.val and root.val>q.val:
			return self.lowestCommonAncestor(root.left,p,q)
		return root



def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    # 实际上inorder 和 postorder一定是同时为空的，因此你无论判断哪个都行
    if not preorder:
        return None
        # 首先获得根节点的值
    root = TreeNode(preorder[0])
    i = inorder.index(root.val)
    root.left = buildTree(preorder[1:i + 1], inorder[:i])
    root.right = buildTree(preorder[i + 1:], inorder[i+1:])
    return root


if __name__=='__main__':
	s = Solution()

	pre = [6,2,0,4,3,5,8,7,9]
	mid = [0,2,3,4,5,6,7,8,9]
	head = buildTree(pre, mid)



	phead  = TreeNode(2)
	n2 = TreeNode(0)
	n3 = TreeNode(4)
	n4 = TreeNode(3)
	n5 = TreeNode(5)

	phead.left = n2
	phead.right = n3

	n3.left = n4
	n4.left = n5


	qhead = TreeNode(8)
	h2 = TreeNode(7)
	h3 = TreeNode(9)

	qhead.left = h2
	qhead.right = h3

	print(s.lowestCommonAncestor(head, phead, qhead).val)


