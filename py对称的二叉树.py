
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def symmetric(self, root):
        if not root:return True

        def helper(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return left.val ==right.val and helper(left.left,right.right) and helper(left.right,right.left)
        return helper(root, root)

if __name__ == "__main__":
    s = Solution()
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(3)
    print(s.symmetric(n2))

