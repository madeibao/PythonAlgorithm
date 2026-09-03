

# 判断是否为对称的二叉树。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def valid(self, root):

        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root, root)


if __name__ == '__main__':
    s = Solution()
    head = TreeNode(1)
    h2 = TreeNode(2)
    h3 = TreeNode(2)

    head.left = h2
    head.right = h3

    print(s.valid(head))

