

class Solution():
    def reverse(self, nums, k):
        res = []
        while nums:
            res.append(nums[:k])
            nums= nums[k:]

        for i in range(len(res)):
            res[i] =res[i][::-1]
        return res

    
if __name__ == '__main__':
    s  = Solution()
    list2= [1,2,3,4,5,6,7,8,9,10,11]
    k =3
    print(s.reverse(list2, k))


# ==============================================================
[[3, 2, 1], [6, 5, 4], [9, 8, 7], [11, 10]]












