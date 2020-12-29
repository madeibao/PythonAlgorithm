
import collections



class Solution(object):
	def mostCommon(self,paragraph,banned):
		l = paragraph.replace(',','').replace('.','').replace('!','').replace('?','').replace(';','').replace("'","").lower()

		a = l.split()

		for i in a:
			if i in banned:
				a.remove(i)

		c =collections.Counter(a)

		for k,v in c.items():
			if v==max(c.values()):
				maxV = k
		return maxV

if __name__=='__main__':
	paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
	banned = ["hit"]

	s = Solution()
	print(s.mostCommon(paragraph, banned))