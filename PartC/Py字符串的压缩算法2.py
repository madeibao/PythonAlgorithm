
class Solution:
    def compressString(self, S: str) -> str:
        ans = ""
        S += " "
        count = 1
        for i in range(1, len(S)):
            if S[i] != S[i-1]:
                ans += S[i-1] + str(count)
                count = 1
            else:
                count += 1
        return ans if len(ans) < len(S)-1 else S[:-1]





class Solution(object):
	def compressString(self,S)->str:
		res = ""

		# 由于需要遍历最后的一个字符，所以临时的添加一个空格字符。
		S+= " "
		count =1
		# 注意的是此时的S的值已经更新了。
		for i in range(1, len(S)):
			if S[i]!=S[i-1]:
				res += S[i-1] +str(count)
				count=1
			else:
				count+=1
		return res if len(res)<len(S) -1 else S[:-1]
