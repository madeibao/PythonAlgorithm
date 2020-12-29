

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([root])
        level = 0
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            level += 1
        return level


if __name__ == "__main__":
    s =Solution()

    n2 = TreeNode(2)
    n3 = TreeNode(1)
    n4 = TreeNode(3)

    n2.left = n3
    n2.right = n4

    print(s.maxDepth(n2))
    
