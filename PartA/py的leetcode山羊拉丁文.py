

class Solution():
	def toGoatLatin(self, S):
		res = []

		def exchange(str2):
			if str2[0] in "aeiouAEIOU":
				str2 = str2+"ma"
			else:
				str2 = str2[1:] +str2[0] + "ma"
			return str2

		list2 = S.split(" ")

		for i in list2:
			res.append(exchange(i))

		res2 = []

		for i in range(len(res)):
			temp = res[i] + (i+1)*"a"
			res2.append(temp)

		return " ".join(res2)

if __name__ == "__main__":
	s = Solution()
	str2 ="I speak Goat Latin"
	print(s.toGoatLatin(str2))

	