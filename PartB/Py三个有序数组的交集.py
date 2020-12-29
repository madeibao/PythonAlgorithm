


#求出三个有序数组的交集的内容



class Solution(object):
    def arraysIntersection(self, A, B, C):
        S = set(A) & set(B) & set(C)
        return sorted(S)

if __name__ == "__main__":
    s = Solution()
    list2 = [1,2,3,4,5]
    list3 = [1,2,3,5,7,9]
    list4 = [2,3,6,7,9,10]
    print(s.arraysIntersection(list2, list3, list4))

