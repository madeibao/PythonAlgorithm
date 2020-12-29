


# 判断是否为亲密的字符串。
# 指的是交换其中的一个字母之后就能变成相等的值。



class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):return False
        if A==B and len(A)>len(set(A)):return True


        ans=[]
        for i in range(len(A)):


            if A[i]!=B[i]:ans.append([A[i],B[i]])


            if len(ans)>2:return False
        if len(ans)<2:return False
        return ans[0][0]==ans[1][1] and ans[1][0]==ans[0][1]

if __name__=='__main__':
    s =Solution()
    A = "aaaaaaabc"
    B = "aaaaaaacb"
    print(s.buddyStrings(A,B))

