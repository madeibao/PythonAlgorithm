


class Solution():
	def isPalindrome(self, s)->bool:

		s2 = s.replace(" ","").lower()
		list2 = []

		for i in range(len(s2)):
			if (ord(s2[i])>=97 and ord(s2[i])<=122) or (ord(s2[i])<=57 and ord(s2[i])>= 48) or (ord(s2[i])>=65 and ord(s2[i])<=90):
				list2.append(s2[i])

		return list2[::-1] == list2



if __name__ == "__main__":
	s =Solution()
	s2 = "A man, a plan, a canal: Panama"
	print(s.isPalindrome(s2))

