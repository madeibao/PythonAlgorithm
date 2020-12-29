# 首先，给你一个初始数组 arr。然后，每天你都要根据前一天的数组生成一个新的数组。
# 第 i 天所生成的数组，是由你对第 i-1 天的数组进行如下操作所得的：

# 假如一个元素小于它的左右邻居，那么该元素自增 1。
# 假如一个元素大于它的左右邻居，那么该元素自减 1。
# 首、尾元素 永不 改变。

# 过些时日，你会发现数组将会不再发生变化，请返回最终所得到的数组。
#----------------------------------------------------------------

from typing import List

class Solution():
    def transformArray(self, arr: List[int]) -> List[int]:  
        change = True
        temp = arr[:]
        n = len(arr)

        while change:
            change = False
            for i in range(1, n-1):
                if arr[i-1] < arr[i] > arr[i+1]:
                    temp[i] -= 1
                    change = True
                elif arr[i-1] > arr[i] < arr[i+1]:
                    temp[i] += 1
                    change = True 
            arr = temp[:]

        return arr 


if __name__ == "__main__":
    s = Solution()
    print(s.transformArray([6,2,3,4]))