


class Solution:
    def binarySearch(self, nums, target):
        # write your code here

        i,j =0, len(nums)-1
        low = i
        high = j

        while low<=high:
            mid = nums[(low+high)//2]
            if mid==target:
                return (low+high)//2
            elif mid<target:
                low = mid+1
            else:
                high = mid-1
        return -1


if __name__=='__main__':
    s = Solution()
    list2 = [1, 2, 3, 3, 4, 5, 10]
    target = 3
    print(s.binarySearch(list2, target))

