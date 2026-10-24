

# @Description: 广度优先搜索，层序遍历, 求最大深度
# @Author: 2026-10-24 15:26:00

from typing import Optional
from TreeNode import TreeNode
from collections import deque
        
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        q = deque([root])
        ans = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:      # 左子节点入队，作为下一层节点
                    q.append(node.left)
                if node.right:     # 右子节点入队，作为下一层节点
                    q.append(node.right)
            ans += 1               # 进入下一层
        return ans

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    print(s.maxDepth(TreeNode(3)))
