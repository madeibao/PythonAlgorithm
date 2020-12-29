

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, mina, maxa):
            if node==None:
                return True
            if node.val<=mina or node.val>=maxa:
                return False
            
            return helper(node.left, mina, node.val) and helper(node.right, node.val, maxa)
            
        return helper(root, float("-inf"), float("inf"))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        def helper(root):
            if not root:
                return 
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res == sorted(res) and len(set(res)) == len(res)

#------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    l2 = TreeNode(1)
    l3 = TreeNode(3)

    root.left = l2
    root.right = l3

    print(s.isValidBST(root))


    #     2 
    #    / \
    #   1   3


