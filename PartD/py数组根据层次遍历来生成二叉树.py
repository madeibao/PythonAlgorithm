
# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/9/26 8:43
# @File: Test

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create(nums):
    root = TreeNode(nums.pop(0))
    que = [root]
    while que:
        node = que.pop(0)
        left = nums.pop(0) if nums else None
        right = nums.pop(0) if nums else None
        node.left = TreeNode(left) if left else None
        node.right = TreeNode(right) if right else None
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return root

def traverse(root):
    if not root: return
    print(root.val)
    traverse(root.left)
    traverse(root.right)

def main():
    # nums = [1, 2, 2, 3, 4, 4, 3]
    nums = [1, 2, 2, None, 3, None, 3]
    root = create(nums)
    traverse(root)

if __name__ == '__main__':
    main()




