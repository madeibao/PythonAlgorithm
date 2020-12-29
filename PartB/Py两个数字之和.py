

# leetcode第一题
# 两个数字之和
# 判断目标数字是否为两个数字的和。


class Solution():
    def SumOfTwo(self,nums,target):
        dic = {}

        for key,value in enumerate(nums):
            if dic.get(target - value) is not None:
            	return [key, dic.get(target - value)]
            dic[value] = key
    	return []


if __name__ == '__main__':
	s = Solution()
	print(s.SumOfTwo([2, 7, 11, 15], 9))






