

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack=[root]
        res=[]
        while stack:
            s=stack.pop()
            res.append(s.val)
            if s.left:#与前序遍历相反
                stack.append(s.left)
            if s.right:
                stack.append(s.right)
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(3)

    n2.right = n3
    n3.left = n4

    print(s.postorderTraversal(n2))

