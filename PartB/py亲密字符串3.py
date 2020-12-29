
# 亲密的字符串，交换两个字符就能变成同一个相同的字符串。


class Solution(object):
	def buddy(self,stra,strb):
		res = []

		if len(stra) == len(strb):
			for i in range(len(stra)):
				if stra[i] !=strb[i]:
					res.append(i)
			if len(res)==2 and stra[res[0]] == strb[res[1]] and stra[res[1]] == strb[res[0]]:
				return True
			if len(res)==0 and len(stra)>len(set(stra)):
				return True
		return False


if __name__ == "__main__":
    s =Solution()
    A= "ab"
    B= "ba"
    print(s.buddy(A, B))