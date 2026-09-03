
class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

from collections import deque
from typing import List

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []

        def bfs(root):
            queue = [root]
            while queue:
                nxt = []
                res.append(queue[-1].val)
                for node in queue:
                    if node.left:
                        nxt.append(node.left)
                    if node.right:
                        nxt.append(node.right)
                queue = nxt
        bfs(root)
        return res

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)

    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n4 = TreeNode(5)
    n5 = TreeNode(4)

    root.left = n2
    root.right = n3

    n2.right = n4
    n3.right = n5
    print(s.rightSideView(root))

