




from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s: str) -> int:
    	dict2 = OrderedDict()
    	for c in s:
    		dict2[c] = dict2[c] +1 if c in dict2 else 1

    	print(dict2)
    	for k,v in dict2.items():
    		if v ==1:
    			return s.index(k)
    	return -1

if __name__ == "__main__":
	str2 ="helloworld"
	s = Solution()
	print(s.firstUniqChar(str2))

