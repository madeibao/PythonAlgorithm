

# 导入链表结构。
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

        # 根据中序和后序来构建二叉树
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 实际上inorder 和 postorder一定是同时为空的，因此你无论判断哪个都行
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.buildTree2(inorder[:i], postorder[:i])
        root.right = self.buildTree2(inorder[i+1:], postorder[i:-1])

        return root

    def preOrder(self,root):
        if not root:
            return []
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)


    def midOrder(self,root):
        if not root:
            return []
        self.midOrder(root.left)
        print(root.val)
        self.midOrder(root.right)


    def postOrder(self,root):
        if not root:
            return []
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val)



if __name__ == "__main__":
    s =Solution()


    inorder2 = [1,2,3,5,6,7,8]
    postorder = [1,3,2,6,8,7,5]

    res2 = s.buildTree2(inorder2, postorder)

    print("--------------------------------------------")
    s.preOrder(res2)



