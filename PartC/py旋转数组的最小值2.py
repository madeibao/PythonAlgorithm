
# 一个数组经过旋转之后的最小值。
# 肯定不是直接的搜索算法。
'''
肯定不能直接遍历，失去了这道题的意义

旋转数组其实是由两个有序数组拼接而成的，因此我们可以使用二分法，只需要找到拼接点即可。
(1)array[mid] > array[high]:

出现这种情况的array类似[3,4,5,6,0,1,2]，此时最小数字一定在mid的右边。
low = mid + 1

(2)array[mid] == array[high]:

出现这种情况的array类似 [1,0,1,1,1] 或者[1,1,1,0,1]，此时最小数字不好判断在mid左边
还是右边,这时只好一个一个试 。
high = high - 1

(3)array[mid] < array[high]:

出现这种情况的array类似[2,2,3,4,5,6,6],此时最小数字一定就是array[mid]或者在mid的左
边。因为右边必然都是递增的。
high = mid
'''

class Solution(object):
    def minNumberInRotateArray(self, nums):
        i, j = 0, len(nums)-1

        while i<j:
            mid = (i+j)//2
            if nums[mid] >nums[j]:
                i = mid+1
            elif nums[mid]<nums[j]:
                j = mid 
            else:
                j-=1
        return nums[i]


if __name__ == "__main__":
    s = Solution()
    list2 = [3,4,5,6,0,0,1,2]
    print(s.minNumberInRotateArray(list2))





