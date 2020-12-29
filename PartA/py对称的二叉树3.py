
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None 
        self.right = None

class Solution:
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, p1, p2):
        if not p1 and not p2: 
            return True
        if not p1 or not p2:    #左右子树都空的情况上面已经排除
            return False
        return p1.val == p2.val and self.isMirror(p1.left, p2.right) and self.isMirror(p1.right, p2.left)


if __name__ == "__main__":
    s =Solution()
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(3) 

    n2.left = n3
    n2.right = n4

    print(s.isSymmetric(n2))

