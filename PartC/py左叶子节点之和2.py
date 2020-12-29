
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumleft(self, root):
        if not root:
            return 0

        # 树的左子树为空， 并且右子树不为空的条件下，返回的是根节点的值。
        if not root.left and root.right:
            return root.val

        res = 0
        left = 0
        if root.left != None and root.left.left == None and root.left.right==None:
            res = root.left.val
        else:
            left = self.sumleft(root.left)

        right = self.sumleft(root.right)
        return left + right + res


if __name__ == '__main__':
    s = Solution()

    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n2.left = n3
    n2.right = n4
    print(s.sumleft(n2))





