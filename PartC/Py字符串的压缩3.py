
# 字符串的压缩的函数
aabcccccaaa
a2b1c5a3



class Solution(object):
	def compress(self,S):
		if len(S)==0:
			return None

		S+= " "
		res = ""
		count =1
		for i in range(1, len(S)):

			if S[i]!=S[i-1]:
				res += S[i-1]+str(count)
				count =1
			else:
				count += 1

		return res if len(res)<len(S[:-1]) else S[:-1]


if __name__ == "__main__":
	s =Solution()	
	str2 = "aabcccccaaa"
	print(s.compress(str2))


