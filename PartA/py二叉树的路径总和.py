
from typing import List

class TreeNode(object):
	def __init__(self,x):
		self.val = x 
		self.left = None
		self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

    	if not root:
    		return False 	

    	# 判断如果左右的叶子节点都为空，只有根节点的条件下。
    	if not root.left and not root.right:
    		return root.val ==sum

    	return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)


# 根据前序和中序来遍历这颗二叉树的值。
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



if __name__ == "__main__":
	s = Solution()


	pre = [5,4,11,7,2,8,13,4,5,1]
	mid = [7,11,2,4,5,13,8,5,4,1]

	head= buildTree(pre, mid)

	print(s.hasPathSum(head ,22))


