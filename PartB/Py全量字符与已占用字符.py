

# python的全量字符和已占用的字符内容


class Solution(object):
	def charSet(self, str2):	

		# 全部字符和已占用的字符。
		data2 = str2.split("@")[0].split(",")
		data3 = str2.split("@")[1].split(",")


		# 已经使用的字符和未被使用的字符。
		allA, usedA = [], []

		# 全部数字和已经使用的数字值。
		allN, usedN = [], []
		res = ""


		# 全部的字符集合。
		for i in data2:
			allA.append(i.split(":")[0])
			allN.append(int(i.split(":")[1]))

		# 已经占用的字符集合。
		try:
			for j in data3:
				usedA.append(j.split(":")[0])
				# 注意的是要把数字来变成整形的。
				usedN.append(int(j.split(":")[1]))
		except:
			pass

		for i in range(len(allA)):
			# 剩余的字符。
			# 临时的定义的变量结果值。
			restA  = allA[i]

			if allA[i] not in usedA:
				resN = allN[i]
			else:
				resN = allN[i] - usedN[usedA.index(allA[i])]

			if resN>0:
				if res=="":
					res =  restA +":"+str(resN)
				else:
					res = res + "," + restA + ":"+ str(resN)
		return res


if __name__ == "__main__":
	s =Solution()
	print(s.charSet("A:3,a:4,b:5,c:2@a:1,b:4"))