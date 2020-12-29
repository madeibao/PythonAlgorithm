'''

def removekletters(ss,k):
	s = []
	ss = list(ss)
	for i in range(len(ss)):
		letter = ss[i]
		while len(s)!=0 and s[len(s)-1]>letter and k>0:
			s.pop(-1)
			k = k-1
		if letter!=0 or len(s)!= 0:
			s.append(letter)

	##当所有字母都扫描完成后，k仍然大于0
	# 那么则从后面来进行弹出的操作。
	while len(s)!=0 and k>0:
		s.pop(-1)
		k = k-1


	## 将最终结果存储为字符串并返回
	result = ''
	result = "".join(list(map(str, s)))

	# result = ''.join(str(i) for i in s)
	return result

ss = input().strip()
k = int(input())
print(removekletters(ss,k))

'''

class Solution():
	def removekletters(self,str2, k):
		res = []
		list2 = list(str2)
		for i in range(len(list2)):
			temp = list2[i]

			while len(res)!=0 and res[len(res)-1]>temp and k>0:
				res.pop(-1)
				k -=1
			if temp!=0 or len(res)!=0:
				res.append(temp)

		while len(res)!= 0 and k>0:
			res.pop(-1)
			k-=1

		return "".join(list(map(str, res)))

if __name__=='__main__':
	s =Solution()
	str2 = input().strip()
	k = int(input())
	print(s.removekletters(str2, k))


