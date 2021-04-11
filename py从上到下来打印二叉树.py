

from collections import deque
from typing import List

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None 


class Solution(object):
    def levelTree(self,root):
        
        res = []
        if not root:return res
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res


if __name__  == "__main__":
    s = Solution()

    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(3)

    n2.left = n3
    n2.right = n4

    print(s.levelTree(n2))

