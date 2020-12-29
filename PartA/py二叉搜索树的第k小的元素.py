
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def help(root,res):
            if root == None:
                return res
            help(root.left, res)
            res.append(root.val)
            help(root.right, res)
        res = []
        help(root, res)
        return res[k-1]

if __name__ == "__main__":

    s = Solution()
    n2 = TreeNode(3)
    n3 = TreeNode(1)
    n4 = TreeNode(4)

    n2.left = n3
    n2.right = n4

    n5 = TreeNode(2)
    n3.right = n5
    print(s.kthSmallest(n2, 1))


# python的另一种的解法，通过迭代器的加持。

class Solution:
    def mid_order(self, root):
        if not root: return
        yield from self.mid_order(root.left)
        yield root.val
        yield from self.mid_order(root.right)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        gen = self.mid_order(root)
        for _ in range(k - 1):
            next(gen)
        return next(gen)

