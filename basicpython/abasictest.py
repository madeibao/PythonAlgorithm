
# for daily practice, just draft some code here

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 节点值，默认 0
        self.next = next    # 指向下一个节点，默认 None

class TreeNode:
    # 初始化二叉树节点：val 为节点值，left/right 为左右子节点引用
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # 节点值，默认 0
        self.left = left      # 左子节点，默认 None
        self.right = right    # 右子节点，默认 None