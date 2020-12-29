


# 翻转字符串的元音的字母的值。
class Solution(object):
	def reversevowel(self,strs):
		left = 0
		right = len(strs)-1

		while True:
			# 循环的终止条件左面的大于右面的指针。
			if right<left:
				break
			while strs[left] not in "aeiouAEIOU" and left<right:
				left +=1
			while strs[right] not in "aeiouAEIOU" and right>left:
				right -=1
			strs[left],strs[right] = strs[right],strs[left]
			left +=1
			right -=1

		return "".join(strs)

if __name__ == "__main__":
	s = Solution()
	str2 = "hello"
	print(s.reversevowel(str2))
	

