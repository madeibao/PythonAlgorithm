



# 返回两个时间的间隔，以照分钟数来返回。
# 



class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        if n > 24*60:
            return 0

        timePoints.sort()
        # 第一个和最后的一个位置上的时间表示进行查询
        h1, m1 = map(int, timePoints[0].split(':'))
        h2, m2 = map(int, timePoints[n-1].split(':'))
        ans = 60*(h1+24-h2)+m1-m2

        for i in range(n-1):
            h1, m1 = map(int, timePoints[i].split(':'))
            h2, m2 = map(int, timePoints[i+1].split(':'))
            diff = 60*(h2-h1)+m2-m1
            ans = min(ans, diff)
        return ans


if __name__ == '__main__':
	s =Solution()
	list2 = ["23:59", "00:00"]
	print(s.findMinDifference(list2))



