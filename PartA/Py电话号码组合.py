

class Solution():
    def getnum(self,a): 
        dic = {
            2:['a', 'b', 'c'],
            3:['d', 'e', 'f'],
            4:['g', 'h', 'i'],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r','s'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y','z'],
        }

        if len(a)==0: return[]

        if len(a)==1: 
            return dic[int(a[0])]

        list2 = []
        result = self.getnum(a[1:])   # 递归的写法。

        for i in result:
            for j in dic[int(a[0])]:
                list2.append(j+i)
        return list2

if __name__=='__main__':
    s = Solution()
    print(s.getnum("23"))



