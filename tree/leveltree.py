
from TreeNode import TreeNode
from typing import List

class Solution:
    def level(self, root: TreeNode | None) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]
        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result

if __name__ == "__main__":
    # 创建一个示例二叉树
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    levels = solution.level(root)
    print(levels)  # 输出: [[1], [2, 3], [4, 5]]