# 给定三个有序的数组，然后求出三个有序数组的交集，求出公共的部分内容。



class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        val = [0] * 2001
        for i in arr1:
            val[i] += 1
        for i in arr2:
            val[i] += 1
        for i in arr3:
            val[i] += 1

       	# 保存结果值。
        res = []

        for i,v in enumerate(val):
            if v == 3:res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    arr1,arr2,arr3 = [1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]
    print(s.arraysIntersection(arr1, arr2, arr3))






