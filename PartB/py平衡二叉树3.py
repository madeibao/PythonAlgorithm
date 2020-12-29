

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def pingheng(self,root):

        def height(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            return max(height(root.left),height(root.right)) + 1

        if not root:
            return True

        if not root.left and not root.right:
            return True

        n2 =height(root.left)
        n3 =height(root.right)

        return abs(n2-n3)<=2 and self.pingheng(root.left) and self.pingheng(root.right)

        

if __name__ == "__main__":
	s = Solution()
	n2 = TreeNode(1)
	n3 = TreeNode(2)
	n4 = TreeNode(3)

	n2.left = n3
	n2.right = n4

    print(s.pingheng(n2))





