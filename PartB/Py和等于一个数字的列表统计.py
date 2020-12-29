


输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]


#================================================================


from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i,j = 0,1
        ret = []
        mid = target // 2 +2
        nums = list(range(1, mid))
        while i <= mid-1 and j<= mid:
            total = sum(nums[i:j])
            if total > target:
                i +=1
            elif total < target:
                j += 1
            else:
                ret.append(nums[i:j])
                i += 1
                j += 1
                
        return ret




if __name__ == "__main__":
	s  = Solution()
	print(s.findContinuousSequence(15))




