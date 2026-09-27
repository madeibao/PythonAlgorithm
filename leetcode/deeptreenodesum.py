

from collections import deque
from TreeNode import TreeNode

class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        
        deque = [root]
        list = []
        while deque:
            res = []
            for _ in range(len(deque)):
                node = deque.pop(0)
                res.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            list.append(res)
        return sum(list[-1])


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.right.right.right = TreeNode(8)

    print(sol.deepestLeavesSum(root))  # Output: 15





