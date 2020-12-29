

# 依照二叉树的方式来进行打家截舍
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dps(tree):
            if tree is None:
                return [0, 0]
            l =  dps(tree.left)
            r = dps(tree.right)
            return [tree.val + l[1] + r[1], max(l) + max(r)]
        return max(dps(root))


if __name__ == "__main__":
	s =Solution()

	n2 = TreeNode(3)
	n3 = TreeNode(2)
	n4 = TreeNode(3)

	n2.left = n3
	n2.right = n4

	nm = TreeNode(3)
	nr = TreeNode(1)

	n3.right = nm
	n4.right = nr

	print(s.rob(n2))


