
class Solution(object):
    def permutate(self, strs):

        if not strs:
            return ""
        res = []
        def helper(start):
            if start == len(strs):
                res.append(strs[:])
            for i in range(start, len(strs)):
                strs[i], strs[start] = strs[start], strs[i]
                helper(start + 1)
                strs[i], strs[start] = strs[start], strs[i]

        helper(0)
        return res


if __name__ == "__main__":
    s = Solution()
    list2 = ['a', 'b', 'c']
    print(s.permutate(list2))







