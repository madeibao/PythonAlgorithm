

# 分发糖果，要求的是比身边分数高的部分，获得的糖果数量也要高。
# 
from typing import List,Tuple
class Solution:
    def candy(self, ratings: List[int]) -> int: 


        # 初始化两个临时的列表的值。
        dp2 = [1 for i in range(len(ratings))]
        dp3 = [1 for i in range(len(ratings))]

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                dp2[i] = dp2[i-1] +1
        
        for j in range(len(dp2)-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                dp3[j] = dp3[j+1] + 1

        res = 0
        for i in range(len(ratings)):
            res += max(dp2[i], dp3[i])

        return res

if __name__ == "__main__":
    s =Solution()
    list3 = [1,0,2]
    print(s.candy(list3))
