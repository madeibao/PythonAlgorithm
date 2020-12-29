
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
import collections


class Solution(object):
    def findMore(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        # 默认的字典的值，
        dict2 = collections.defaultdict(int)
        res = []
        res.append(root)

        while res:
            temp = res.pop()
            dict2[temp.val] += 1

            if temp.right:
                res.append(temp.right)
            if temp.left:
                res.append(temp.left)

        maxValue = max(dict2.values())

        return [k for k, v in dict2.items() if v == maxValue]


if __name__ == "__main__":
    s = Solution()
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(2)

    n2.left = n3
    n2.right = n4
    print(s.findMore(n2))



