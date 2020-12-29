
class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


class Solution(object):
    def getSumLeft(self, head):
        if not head:
            return 0

        cur, left, right = 0, 0, 0
        if head.left!=None and head.left.left==None and head.left.right==None:
            cur = head.left.val
        else:
            left = self.getSumLeft(head.left)
        right = self.getSumLeft(head.right)
        return cur+left + right


if __name__=='__main__':
	s = Solution()

	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(4)

	n2.left = n3
	n2.right = n4

	print(s.getSumLeft(n2))










