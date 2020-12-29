# Definition for a binary tree node.
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res


if __name__ == "__main__":
    s = Solution()

    root = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)

    mn3 = TreeNode(4)
    mn4 = TreeNode(5)

    root.left = l2
    root.right = l3

    l2.left = mn3
    l2.right = mn4

    print(s.levelOrder(root))




