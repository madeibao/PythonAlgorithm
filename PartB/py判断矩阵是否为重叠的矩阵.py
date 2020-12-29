


#-----------------------------------------------------------------------------
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。

如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形，判断它们是否重叠并返回结果。

def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    return not (rec1[2] <= rec2[0] or  # 1右<2左
                rec2[2] <= rec1[0] or  # 2右<1左
                rec1[3] <= rec2[1] or  # 1上<3下
                rec2[3] <= rec1[3])  # 3上<1下



def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    x_overlap = not(rec1[2] <= rec2[0] or rec2[2] <= rec1[0])
    y_overlap = not(rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
    return x_overlap and y_overlap




if __name__ == "__main__":
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]
    print(isRectangleOverlap(rec1, rec2))


