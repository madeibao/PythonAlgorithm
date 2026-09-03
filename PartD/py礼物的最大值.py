


# 礼物的最大值。
# 从左上角的路径上到右下角的路径上获得的最大礼物之和。


class Solution(object):
    def maxValue(self,gift):
        m = len(gift)
        n = len(gift[0])
        res = [[0]* (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                res[i][j] = gift[i-1][j-1] + max(res[i-1][j], res[i][j-1])
        return res[m][n]
        

if __name__ == "__main__":
    s = Solution()

    nums = [
        [1,3,1],
        [1,5,1],
        [4,2,1],
    ]

    print(s.maxValue(nums))




