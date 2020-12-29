
# 仅仅把字符串中的字母来进行翻转，其他的字符不进行变化。


class Solution:
	class Solution(object):
	    def reverseOnlyLetters(self, S):
	        """
	        :type S: str
	        :rtype: str
	        """
	        S = list(S)
	        front, end = 0, len(S) - 1
	        while front < end:
	            if not S[front].isalpha():
	                front += 1
	            elif not S[end].isalpha():
	                end -= 1
	            else:
	                S[front], S[end] = S[end], S[front]
	                front += 1
	                end -= 1
	        return "".join(S)




if __name__ == "__main__":
	s =Solution()
	list2 ="ab-cd"
	print(s.reverseOnlyLetters(list2))


