
# 验证IP地址
# @param IP string字符串 一个IP地址字符串
# @return string字符串
class Solution:
    def solve(self , IP ):
        a=IP.strip().split(".")
        b=IP.strip().split(":")
        if "." in IP and len(a)<4 or len(a)>4 or "" in a:
            return "Neither"
        elif ":" in IP and len(b)<8 or len(b)>8 or "" in b:
            return "Neither"
        elif len(a)==4:
            for s in a:
                if int(s)>=255 or s[0]=="0":
                    return "Neither"
            return "IPv4"
        elif len(b)==8:
            for s in b:
                if len(s)>=2 and s[0]=="0" and s[2]=="0" or len(s)>4:
                     return "Neither"
            return "IPv6"
                
if __name__ == "__main__":
	s = Solution()
	str2 ="2001:0db8:85a3:0:0:8A2E:0370:7334"
	print(s.solve(str2))
