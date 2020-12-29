



class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxHeight(self,root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return max(self.maxHeight(root.left),self.maxHeight(root.right)) +1


if __name__ == "__main__":
    s =Solution()

    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n2.left =n3
    n2.right = n4

    print(s.maxHeight(n2))


