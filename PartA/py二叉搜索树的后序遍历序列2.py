

# 给定数组判断是否为后序遍历序列。

class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


if __name__ == "__main__":
    s = Solution()
    nums = [1,3,2,6,5]
    print(s.verifyPostorder(nums))

