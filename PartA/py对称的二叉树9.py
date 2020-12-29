

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None 
        self.right = None


class Solution(object):
    def minTree(self,root):

        def symmetric(left, right):
            if not left or not right:
                return True 
            if not left or not right:
                return False

            return left.val ===right.val and symmetric(left.left, right.right) and symmetric(left.right, right.left)

        return symmetric(root.left, root.right)


if __name__ == "__main__":
    s = Solution()
    n2 =TreeNode(2)
    n3 =TreeNode(3)
    n4 =TreeNode(3)

    n2.left = n3
    n2.right = n4

    print(s.minTree(n2))

    