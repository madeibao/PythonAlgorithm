


class Solution:
    def numberOf2sInRange(self, n: int) -> int:

    	res = 0
    	for i in range(n+1):
    		if str(i).find('2')!=-1:
    			res +=1
    	return res

    	

if __name__ == "__main__":
	s =Solution()
	n = 25
	print(s.numberOf2sInRange(n))



















