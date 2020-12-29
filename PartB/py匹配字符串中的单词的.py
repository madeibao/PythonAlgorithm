

class Solution():
	def numMatchingSubseq(self,S:str,words):

		count = 0
		for i in words:
			num = 0
			pos = -1

			for j in i:

				# pos代表的是开始的单词的位置。


				
				pos = S.find(j, pos+1)
				if pos==-1:
					break
				else:
					num+=1
			if num==len(i):
				count+=1
		return count

if __name__=='__main__':
	s =Solution()
	S ="abcde"
	words =["a","bb","acd","ace"]
	print(s.numMatchingSubseq(S,words))



