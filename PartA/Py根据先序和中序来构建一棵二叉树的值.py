
# 导入链表结构。
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        # 首先获得根节点的值
        root = TreeNode(preorder[0])

        i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i+1:])

        return root


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
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    res = s.buildTree(preorder, inorder)

    s.preOrder(res)

    inorder2 = [9,3,15,20,7]
    postorder = [9,15,7,20,3]

    res2 = s.buildTree2(inorder2, postorder)

    print("--------------------------------------------")
    s.preOrder(res2)


    print("---------------自己的二叉树-----------------------------------")
    n5 = TreeNode(5)
    n2 = TreeNode(2)
    n7 = TreeNode(7)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n8 = TreeNode(8)

    n5.left = n2
    n5.right = n7

    n2.left = n1
    n2.right = n3

    n7.left = n6
    n7.right = n8

    print("前序序列")
    s.preOrder(n5)
    print("------------------------------------")
    print("中序序列")
    s.midOrder(n5)
    print("后序序列")
    print("-----------------------------------------")
    s.postOrder(n5)
