



class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sum2 = 0	
        list2 = list(s)
        balance = 0

        for i in range(0, len(list2)):
        	if list2[i] == 'L':
        		balance -= 1
        	elif list2[i] == 'R': 
        		balance += 1 
        	if balance == 0:
        		sum2 += 1

       	if sum2 ==  0:
       		return 1
       	else:
       		return sum2

if __name__=='__main__':

	s = Solution()
	s2 = "RLRRLLRLRL"
	print(s.balancedStringSplit(s2))

	
