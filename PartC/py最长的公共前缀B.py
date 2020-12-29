



class Solution(object):
    def longestPrefix(self,strs):

        res = str()
        for i in zip(*strs):
            if len(set(i))==1:
                res+=i[0]
        return res 


if __name__=='__main__':
    s = Solution()
    list2 = ["flower","flow","flight"]
    print(s.longestPrefix(list2))

