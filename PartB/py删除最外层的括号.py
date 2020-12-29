



# 删除最外层的括号的匹配的结果值。


class Solution:
    def removeOuterParentheses(self, S: str) -> str:    
        stack2 =[]
        res = ""
        temp = ""
        for i in range(len(S)):
            if S[i]=='(': 
                stack2.append(S[i])
            else:
                stack2.pop()
            temp+=S[i]
            if not len(stack2):
                res+=temp[1:-1]
                temp = ""

        return res 


if __name__=="__main__":
    s =Solution()
    str2 ="(()())(())"
    print(s.removeOuterParentheses(str2))

 
