

class Solution():
    def isIsomorphic(self, s: str, t: str) -> bool:

    	if len(s)!=len(t):
    		return False
    	if len(set(s))!=len(set(t)):
    		return False 
    	if len(set(zip(s,t)))== len(set(t)):
    		return True
    	else:
    		return False

if __name__ == "__main__":
	s = Solution()
	s2 ='abb'
	s3 = 'egg'
	print(s.isIsomorphic(s2,s3))