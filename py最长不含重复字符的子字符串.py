



class Solution(object):
    def subStr2(self,strs):

        res = []
        temp = 0
        for i in strs:
            while i in res:
                res.pop(0)
            res.append(i)
            temp = max(temp,len(res))

        return temp

if __name__ == "__main__":
    s = Solution()
    str2 = "abcabcbb"
    print(s.subStr2(str2))

