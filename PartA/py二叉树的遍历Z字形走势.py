

from collections import deque

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def travel(self, root):

        queue2 = deque()
        res = []
        queue2.append(root)
        if not root:
            return res

        while queue2:
            len2 = len(queue2)
            temp = []
            for i in range(len2):
                node = queue2.popleft()
                temp.append(node.val)
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            res.append(temp)

            # 根据统计结果来进行逆置。
            for i in range(len(res)):
                if i % 2 == 1:
                    res[i] = res[i][::-1]
        return res


if __name__ == "__main__":
    s = Solution()
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n2.left = n3
    n2.right = n4
    print(s.travel(n2))


