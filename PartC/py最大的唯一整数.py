

class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import Counter
        dic = Counter(A)

        res = -1
        for key, val in dic.items():
            if val == 1:
                res = max(res, key)
        return res


if __name__ == "__main__":
    s = Solution()
    list2 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    print(s.largestUniqueNumber(list2))

