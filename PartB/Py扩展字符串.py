


# 查找常用的字符串的值。

class Solution():
    def extension(self,strs):
        set2 = list(set(strs[0]))
        res = []

        temp = ""
        for i in set2:
            temp = min(j.count(i) for j in strs)
            res+=temp*i

        return res 
        
if __name__ == "__main__":
	s = Solution()
	list2 =["bella","label","roller"]
    print(s.extension(list2))


