
from TreeNode import TreeNode

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node: TreeNode) -> (int, int):
            if not node:
                return 0, 0
            l_sum, l_count = dfs(node.left)
            r_sum, r_count = dfs(node.right)
            cur_sum = l_sum + r_sum + node.val
            cur_count = l_count + r_count + 1
            nonlocal ans  # 使用nonlocal关键字来修改外部变量ans的值
            ans += cur_sum // cur_count == node.val
            return cur_sum, cur_count
        
        dfs(root)
        return ans

if __name__ == "__main__":
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)

    print(Solution().averageOfSubtree(a))
        