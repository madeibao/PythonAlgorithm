
# # python 判断矩形是否重叠的内容。
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
# 给出两个矩形，判断它们是否重叠并返回结果。

from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        right = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        return left > 0 and right > 0



    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # 长和宽的坐标都分别相交

        x1, y1, x2, y2 = rec1  # 依照元组的形式来进行整体的赋值。
        x3, y3, x4, y4 = rec2
        return (x3 - x2) * (x4 - x1) < 0 and (y3 - y2) * (y4 - y1) < 0

   


if __name__ == '__main__':
    s = Solution()
    print(s.isRectangleOverlap([0,0,2,2], [1,1,3,3]))
    print(s.isRectangleOverlap([0,0,1,1], [1,0,2,1]))














