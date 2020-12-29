
from typing import List

class TreeNode(object):
	def __init__(self,x):
		self.val =x
		self.left = None 
		self.right = None

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


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        
        def dfs(root,tmp,sum):
            if not root: return 
            
            if not root.left and not root.right and root.val == sum:
                tmp += [root.val]
                self.res.append(tmp)
            
            dfs(root.left,tmp + [root.val], sum - root.val)
            dfs(root.right,tmp + [root.val], sum - root.val)

        dfs(root, [], sum)
        return self.res

class Solution():
	def pathSum(self, root, sum):
		self.res = []

		def dfs(root, temp, sum):
			if not root:return

			if not root.left and not root.right and root.val ==sum:
				temp+= [root.val]
				self.res.append(temp)

			dfs(root.left, temp+[root.val], sum-root.val)
			dfs(root.right, temp+[root.val], sum-root.val)

		dfs(root, [] ,sum)
		return self.res


if __name__=='__main__':
	s = Solution()

	pre = [5,4,11,7,2,8,13,4,5,1]
	mid = [7,11,2,4,5,13,8,5,4,1]

	head= buildTree(pre, mid)

	res = s.pathSum(head, 22)

	print(res)

