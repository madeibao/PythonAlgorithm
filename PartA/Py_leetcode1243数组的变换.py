

from typing import List


# class Solution():
#     def transformArray(self, arr: List[int]) -> List[int]:
#         change, tmp, n = True, arr[:], len(arr)
#         while change:
#             change = False
#             for i in range(1, n - 1):
#                 if arr[i - 1] < arr[i] > arr[i + 1]:
#                     tmp[i] -= 1
#                     change = True
#                 elif arr[i - 1] > arr[i] < arr[i + 1]:
#                     tmp[i] += 1
#                     change = True
#             arr = tmp[:]
#         return arr


class Solution():
    def transformArray(self, arr):
        change = True 
        temp = arr[:]
        n = len(arr)

        while change:
            change = False
            for i in range(1, n-1):
                if arr[i-1]< arr[i] > arr[i+1]:
                    temp[i] -= 1
                    change = True
                elif arr[i-1] > arr[i] < arr[i+1]:
                    temp[i] += 1
                    change = True
            arr = temp[:]
        return arr



if __name__ == "__main__":
    s = Solution()
    print(s.transformArray([1,6,3,4,3,5]))
        