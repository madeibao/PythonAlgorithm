
'''
题目描述
牛牛有一个n个数字的序列a_1,a_2,\dots,a_na 
1
​	
 ,a 
2
​	
 ,…,a 
n
​	
 ，现在牛牛想把这个序列分成k段连续段，牛牛想知道分出来的k个连续段的段内数字和的最小值最大可以是多少？
示例1
输入
复制
4,2,[1,2,1,5]
输出
复制
4
说明
有3种分法
[1],[2,1,5]，数字和分别为1，8，最小值为1
[1,2][1,5]，数字和分别为3，6，最小值为3
[1,2,1],[5]数字和分别为4，5，最小值为4
则最小值的最大值为4
'''


# ===================================================================================================
class Solution:
    def solve(self, n, k, a):
        x, y = 0, sum(a)
        if k == 1:
            return y
            
        while y - x > 1:
            mid = (x + y) / 2
            segment = 0
            nowval = 0
            for i in range(len(a)):
                nowval += a[i]
                if nowval >= mid:
                    segment += 1
                    nowval = 0
            if segment >= k:
                x = mid
            else:
                y = mid
        return round((x + y) / 2)

if __name__ == "__main__":
	s = Solution()
	n, k = map(int, input().split(" "))
	res = list(map(int, input().split(" ")))
	print(s.solve(n, k ,res))