给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。

 
示例 1：

输入：[2,1,2]
输出：5

示例 2：

输入：[1,2,1]
输出：0

示例 3：

输入：[3,2,3,4]
输出：10


示例 4：

输入：[3,6,2,3]
输出：8


# 三角形面积的最大的周长。
class Solution():
    def largestPerimeter(self, A) -> int:

        if len(A)==3 and not self.isTriange(A):
            return 0
        elif len(A)==3 and self.isTriange(A):
            return sum(A)
        else:
            num2 = sorted(A)
            num3 = []

            for i in range(len(num2)-2):
                num4 = []
                num4.append(num2[i])
                num4.append(num2[i+1])
                num4.append(num2[i+2])
                num3.append(num4)

            num5 = []
            for i in num3:
                if self.isTriange(i):
                    num5.append(sum(i))
            if len(num5)!= 0:
                return max(num5)
            else:
                return 0

    def isTriange(self, B):
        if B[0]+B[1]>B[2] and B[0]+B[2]>B[1] and B[1]+B[2]>B[0] and B[0]-B[1]<B[2] and B[0]-B[2]<B[1] and B[2]-B[1]<B[0]:
            return True
        else:
            return False


num3 = [1, 1, 2, 3, 5]
cc = Solution()
print(cc.largestPerimeter(num3))


#-----------------------------------------------------------------------------------
#  另一种写法


class Solution:
    def largestPerimeter(self, A) -> int:

        # 首先排好序。
        num2 = sorted(A)  
        temp = 0
        for i in range(len(num2)-1, 1, -1):
            a = num2[i]
            b = num2[i-1]
            c = num2[i-2]
            if a < b+c:     # 从最大的地方开始循环的操作。
                temp = a+b+c
                break       # 只要找到符合条件的地方就终止操作。


        if temp != 0:
            return temp
        else:
            return 0


num3 = [1, 2, 2]
cc = Solution()
print(cc.largestPerimeter(num3))
