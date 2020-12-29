


# class Solution(object):
#     def canPermutePalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         record = dict()
#         for i, char in enumerate(s):
#             record[char] = record.get(char, 0) + 1
        
#         odd_cnt = 0
#         for key, val in record.items():
#             if val % 2:
#                 odd_cnt += 1
#                 if odd_cnt > 1:
#                     return False
#         return True



# 就是判断其中的奇数的数字的出现的次数，如果大于1次，就不可能出现更好的结果值。
from collections import Counter

class Solution(object):
	def canPermutePalindrome(self,s):
		dict2 = dict(Counter(s))

		cnt = 0;

		for key, value in dict2.items():
			if value%2:
				cnt += 1
				if cnt >1:
					return False	

		return True 



if __name__ == "__main__":

	s =Solution()
	print(s.canPermutePalindrome("aabb"))
