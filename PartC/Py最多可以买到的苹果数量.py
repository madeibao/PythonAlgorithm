class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # 首先来进行排序的操作,然后来进行下一步。
        arr.sort()
        s = 0
        for i, w in enumerate(arr):
            if s + w > 5000:
                return i
            s += w
        return len(arr)

if __name__ == "__main__":
    s =Solution()
    arr = [900,950,800,1000,700,800]
    print(s.maxNumberOfApples(arr))