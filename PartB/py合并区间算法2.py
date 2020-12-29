

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        res = []

        # 首先按照左面的边界值来进行排序操作。
        intervals.sort(key=lambda x: x[0])  # 先按区间左边界值由小到大排序
        for inter in intervals:
            if len(res) == 0 or res[-1][1] < inter[0]:  # 如果结果集最后一个元素的右边界比新加入区间的左边界小，直接加入结果集
                res.append(inter)
            else:  # 否则，说明新加入的和结果集最后一个区间有重合，更新区间右边界即可
                res[-1][1] = max(res[-1][1], inter[1])
        return res


if __name__ == "__main__":
    s = Solution()
    list2 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(s.merge(list2))





