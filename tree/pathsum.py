

from typing import List
from TreeNode import TreeNode

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        self.res = []

        def dfs(node: TreeNode | None, temp: List[int], remaining_sum: int):
            if not node:
                return

            # 如果是叶子节点，且当前节点值等于剩余目标值，说明找到了一条路径
            if node.left is None and node.right is None:
                if node.val == remaining_sum:
                    self.res.append(temp + [node.val])
                return

            # 继续向下递归，剩余目标值减去当前节点的值
            dfs(node.left, temp + [node.val], remaining_sum - node.val)
            dfs(node.right, temp + [node.val], remaining_sum - node.val)

        dfs(root, [], targetSum)
        return self.res

if __name__ == '__main__':
    # 构建测试用例
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    targetSum = 22
    # 预期输出: [[5,4,11,2], [5,8,4,5]]
    print(Solution().pathSum(root, targetSum))