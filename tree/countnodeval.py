

from TreeNode import TreeNode
from typing import List
import collections
from collections import deque

class Solution:
    def countNode(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        d = deque([root])
        count = 0
        while d:
            node = d.popleft()
            if node:
                count += node.val
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return count


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().countNode(root))