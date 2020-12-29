

# # 两个字符串的数字来相加求和。



class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans=[0]
        len1,len2,carry=len(num1),len(num2),0
        for i in range(1,max(len1,len2)+1):
            n1=int(num1[-i]) if i<=len1 else 0
            n2=int(num2[-i]) if i<=len2 else 0
            sum=n1+n2+carry
            carry=sum//10
            ans.insert(0,str(sum%10))
        return ''.join(ans[:-1]) if carry==0 else '1'+''.join(ans[:-1])



if __name__=='__main__':
	s =Solution()
	str2 ="123"
	str3 ="123"
	print(s.addStrings(str2,str3))






