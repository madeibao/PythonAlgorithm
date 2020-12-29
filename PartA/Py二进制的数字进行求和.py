# # 给定两个二进制的表示的数字，然后求出和，并且仍然依照二进制的形式来给出最终的结果内容。


# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         i, j = len(a) - 1, len(b) - 1
#         res = ''
#         carry = 0
#         # 从尾到头对位相加
#         while i >= 0 or j >= 0:
#             n1 = int(a[i]) if i >= 0 else 0
#             n2 = int(b[j]) if j >= 0 else 0
#             tmp = n1 + n2 + carry
#             # 二进制进位
#             carry = tmp // 2
#             res = str(tmp % 2) + res
#             i, j = i - 1, j - 1
#         # 最高位如果有进位，需要加上carry
#         return res if not carry else '1' + res


# if __name__ == "__main__":
#     s = Solution()
#     print(s.addBinary("110", "110"))





class Solution(object):
	def addBinary(self,num1, num2):


		carry = 0
		len1 = len(num1)-1
		len2 = len(num2)-1

		while len1>=0 and len2>=0:
			a= int(num1[i]) if len1>=0 else 0
			b= int(num2[i]) if len2>=0 else 0

			temp = a+b+carry
			carry = = temp//2

			res = str(temp%2) + res
			len1 = len1-1
			len2 = len2-1

		return res if not carry else '1'+res


if __name__ == "__main__":
	s= Solution()
	str2 ="101"
	str3 ="110"

	print(s.addBinary(str2,str3))

	