

class Solution():
	def reverse(self, s):
		list2 = s.strip().split(" ")
		list2.reverse()
		return " ".join(list2)


if __name__ == "__main__":
	s =Solution()
	print(s.reverse("the sky is blue"))