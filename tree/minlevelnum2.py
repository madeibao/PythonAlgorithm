

from TreeNode import TreeNode
from typing import List
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> List[List[int]]:
    	if not root:
    		return 0

    	q = deque([root])
    	ans = 1
    	level = 1
    	minNum = float('inf')

    	while q:
    		level_num = 0
    		count = len(q)
    		for _ in range(count):
    			nodea = q.popleft()
    			level_num+=nodea.val
    			if nodea.left:
    				q.append(nodea.left)
    			if nodea.right:
    				q.append(nodea.right)
    		if level_num<minNum:
    			minNum = level_num
    			ans = level
    		level+=1
    	return ans

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    res = Solution().levelOrder(root)
    print(res)


