
class Solution():
    def dominantIndex(self,nums):
        maxNum = max(nums)

        index2 = 0
        
        for i in nums:
            if i==maxNum:
                continue
            elif maxNum < i*2:
                index2  -1
                break
            else:
                index2 = nums.index(maxNum)
        return index2


if __name__ == "__main__":
    s = Solution()  
    print(s.dominantIndex([3,6,1,0]))

