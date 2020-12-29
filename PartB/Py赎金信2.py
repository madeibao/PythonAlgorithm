

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

    	ran = list(ransomNote)
    	mag = list(magazine)


    	for i in ran:
    		if i in mag:
    			mag.remove(i)
    		else:
    			return False 
    	return True	


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("aa","ab"))
    print(s.canConstruct("aa","aab"))

