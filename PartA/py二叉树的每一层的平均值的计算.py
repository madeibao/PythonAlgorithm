
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageLevel(self, root):
        if not root:
            return []
        queue2 = deque([root])
        res = []
        while queue2:
            temp = 0
            n = len(queue2)
            for _ in range(n):
                node = queue2.popleft()
                temp += node.val
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            res.append(temp /n)
        return res

if __name__ == "__main__":
    s = Solution()

    n2 = TreeNode(2)
    n3 = TreeNode(4)
    n4 = TreeNode(6)

    n2.left = n3
    n2.right = n4
    print(s.averageLevel(n2))





