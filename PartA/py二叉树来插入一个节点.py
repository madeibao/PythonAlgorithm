
class TreeNode(object):
    def __init__(self, x=0, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root


def preorder(root):
    if not root:
        return []

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


if __name__ == "__main__":
    s = Solution()

    head = TreeNode(4)

    l2 = TreeNode(2)
    r2 = TreeNode(7)

    l23 = TreeNode(1)
    l24 = TreeNode(3)

    l2.left = l23
    l2.right = l24

    head.left = l2
    head.right = r2
    val = 5
    res = s.insertIntoBST(head, val)
    preorder(res)

