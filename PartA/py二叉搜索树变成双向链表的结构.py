

class TreeNode(object):
	def __init__(self,x):
		self.val =x
		self.left = None
		self.right = None


class Solution:
    def treeToDoublyList(self, root):
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def midTraverse(node):
            if node is None:
                return []
            result = midTraverse(node.left)+[node]+midTraverse(node.right)
            return result
        sorted_list = midTraverse(root)

        if len(sorted_list)==0:
            return None
        if len(sorted_list)==1:
            root.left = root
            root.right = root
            return root

        for i in range(len(sorted_list)):
            node = sorted_list[i]
            if i==0:
                node.right = sorted_list[i+1]
                node.left = sorted_list[-1]
            elif i==len(sorted_list)-1:
                node.left = sorted_list[i-1]
                node.right = sorted_list[0]
            else:
                node.left = sorted_list[i-1]
                node.right = sorted_list[i+1]

        return sorted_list[0]




if __name__ == "__main__":

	root = TreeNode(4)
	l2 = TreeNode(2)
	l3 = TreeNode(5)

	root.left = l2
	root.right = l3

	n2 = TreeNode(1)
	n3 = TreeNode(2)

	l2.left = n2
	l2.right = n3

	s =Solution()
	res = s.treeToDoublyList(r)
	print(res)

