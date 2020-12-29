

class Solution():
    def climStair(self,n:int)->int:  
        if n<1: return 0
        memory = {}   # 创建一个空的字典。

        memory[1]= 1
        memory[2]= 2

        for i in range(3, n+1):
            memory[i]= memory[i-1]+memory[i-2]
        return memory memory[n]

    
# 解法二

class Solution():   
    def climStair(self, n):
        if n<1: return 0

        p = 1
        q = 2
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(2,n):
            p,q = q,p+q
            
        return q


if __name__ == "__main__":

    s= Solution():
    print(s.climStair[5])