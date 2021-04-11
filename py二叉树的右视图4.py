
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
	def rightview(self,root):

		res = []
		queue = deque()
		while queue:
			n = len(queue)
			for i in range(n):
				node = queue.popleft()
				if i ==n-1:
					res.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
		return res


if __name__ == "__main__":
    s = Solution()

    root = TreeNode(1)

    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n4 = TreeNode(5)
    n5 = TreeNode(4)

    root.left = n2
    root.right = n3

    n2.right = n4
    n3.right = n5

    print(s.rightSideView(root))

    

