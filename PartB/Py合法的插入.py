

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:

    	def validDelete(str1, str2):
    		m = len(str1)
    		n = len(str2)

    		# 默认的条件是 m>n

    		begin = 0
    		while begin < n and str1[begin]==str2[begin]:
    			begin += 1 

    		begin += 1

    		while begin < m and str1[begin]==str2[begin-1]:
    			begin += 1 

    		return begin>=m

    	if abs(len(str1) - len(str2))==1:
    		return validDelete(first, second)

    	# 方法2的内容，
    	def validDelete2(first, second):
    		if abs(len(first)-len(second))==1:#插入/删除字符
            if len(first)>len(second):
                longer=first
                shorter=second
            else:
                longer=second
                shorter=first
            for i in range(len(shorter)):
                j=i
                if longer[j]!=shorter[i]:
                    j+=1
                    if longer[j]!=shorter[i]:
                        return False
            return True


if __name__=="__main__":
	s = Solution()
	str1 = "pale"
	str2 = "pal"

	print(s.oneEditAway(str1, str2))

