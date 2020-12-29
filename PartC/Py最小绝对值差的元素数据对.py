from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        list2 = []
        arr2 = sorted(arr)
        for i in range(1, len(arr2)):
            list2.append(arr2[i]- arr2[i-1])
        
        # 获取最小值。
        temp = min(list2)

        list3 = []

        for i in range(1, len(arr2)):
            list4 = []
            if arr2[i] - arr2[i-1] == temp:
                list4.append(arr2[i-1])
                list4.append(arr2[i])
            if len(list4):
                list3.append(list4)
        return list3

if __name__ == "__main__":

    list2 = [4,2,1,3]
    s = Solution()  
    print(s.minimumAbsDifference(list2))






