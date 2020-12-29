
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def maxDepth(self,root):

        if not root:
            return 0
        if root.left==None and root.right==None:
            return 1        
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) +1


if __name__=='__main__':
    s =Solution()
    n2 =TreeNode(2)
    n3 =TreeNode(3)
    n4 =TreeNode(4)

    n2.left = n3    
    n2.right= n4

    print(s.maxDepth(n2))