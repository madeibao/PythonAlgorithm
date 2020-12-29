
# 判断两个字符串是否为同构的字符串类型


class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
    	if len(s)!=len(t): return False
    	if len(set(s))!=len(set(t)): return False

    	if(len(set(zip(s,t)))==len(set(t))):
    		return True
    	else:
    		return False 


if __name__=='__main__': 
	s = Solution()	
	print(s.isIsomorphic("egg","abb"))




