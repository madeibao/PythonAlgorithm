
from collections import deque

# 定义基础的二叉树的结构。

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def level(self,head):
        if not head:
            return []
        queue = deque()
        queue.append(head)

        res = []
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res 


if __name__ == "__main__":
    s = Solution()


    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n2.left = n3
    n2.right = n4
    print(s.level(n2))

