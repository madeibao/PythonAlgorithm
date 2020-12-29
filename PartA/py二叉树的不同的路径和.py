
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def different(self, root, target):
        self.res = []

        def dfs(root, temp, target):
            if not root:
                return

            if not root.left and not root.right and root.val == target:
                temp+=[root.val]
                self.res.append(temp)

            dfs(root.left,temp+[root.val],target-root.val)
            dfs(root.right,temp+[root.val],target-root.val)

        dfs(root,[], target)
        return self.res


if __name__ == "__main__":
    s =Solution()

    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(3)

    n2.left = n3
    n2.right = n4
    target = 5

    print(s.different(n2, target))






