



# 求一个字符串列表的最长的公共的前缀的值。


class Solution():
    def mostCommon(self,strs):
        res = ""

        for i in zip(*strs):
            if len(set(i))==1:
                res += i[0]
    
        return res
if __name__ == "__main__":
    s = Solution()
    list2 = ["flower","fly","flow"]
    print(s.mostCommon(list2))


