'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
通过次数90,421提交次数213,377

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
#-----------------------------------------------------------------
#-----------------------------------------------------------------

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])  # 先按区间左边界值由小到大排序

        for inter in intervals:
            if len(res) == 0 or res[-1][1] < inter[0]:  # 如果结果集最后一个元素的右边界比新加入区间的左边界小，直接加入结果集
                res.append(inter)
            else:  # 否则，说明新加入的和结果集最后一个区间有重合，更新区间右边界即可
                res[-1][1] = max(res[-1][1], inter[1])
        return res


if __name__ == '__main__':
	temp = [[1,3],[2,6],[8,10],[15,18]]
	s = Solution()
	print(s.merge(temp))





