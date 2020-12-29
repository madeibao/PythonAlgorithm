

给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。


示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List

class Solution():
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return []
        if len(a)==1:
            return [0]
        b=[1]*len(a)
        for i in range(len(b)-2,-1,-1):
            b[i]=b[i+1]*a[i+1]
        tmp=a[0]
        for j in range(1,len(a)):
            b[j]=tmp*b[j]
            tmp=tmp*a[j]
        return b


if __name__ == "__main__":
	s = Solution()
	print(s.constructArr([1,2,3,4,5,]))
	print(s.constructArr([1,2,0,4,0,]))