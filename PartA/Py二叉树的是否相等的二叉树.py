

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        return Solution.equiv(root1, root2)

    @staticmethod
    def equiv(r1, r2):
        if r1 is None:
            return r2 is None
        elif r2 is None:
            return False

        if r1.val != r2.val:
            return False

        return (Solution.equiv(r1.left, r2.left) and Solution.equiv(r1.right, r2.right)) \
               or (Solution.equiv(r1.left, r2.right) and Solution.equiv(r1.right, r2.left))


if __name__ == '__main__':
    s = TreeNode(1)
    s2 = TreeNode(2)
    s3 = TreeNode(3)
    s.left = s2
    s.right = s3

    n = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n.left = n2
    n.right = n3

    test= Solution()
    print(test.equiv(s, n))
