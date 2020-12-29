
'''

abc 

bca 

字符串中的字符经过重新的排列，来得到另外的一个字符。
'''

class Solution():
    def restore(self,str2,str3):
        return True if(sorted(str2)==sorted(str3)) else False


if __name__ == "__main__":
    s2 = "abc"
    s3 = "bca"
    s4 = Solution()
    print(s4.restore(s2,s3))



