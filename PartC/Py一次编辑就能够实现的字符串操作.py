

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
    	if len(first) - len(second) >= 2 or len(second) - len(first) >= 2:
    		return False

    	if first == second:
    		return True 

    	list1 =list(first)
    	list2 =list(second)

    	def validReplace(list1, list2):

	    	# 下面的是判断是否只有一个字符的变化，还是多个字符的变化。
	    	temp = []
	    	res = 0

	    	for i,j in zip(list1,list2):
	    		temp.append([i,j])

	    	for i in temp:
	    		if i[0]!=i[1]:
	    			res += 1
	    	if res==1:
	    		return True
	    	return False


    	# 是否为和合理的插入和删除元素内容。
    	# 前提是始终保持的是m大于n的条件。
    	def validDelAndInsert(list1,list2):
    		m = len(list1)
    		n = len(list2)
    	# m>n 默认的。
    		begin = 0
    		while begin<n and list1[begin]== list2[begin]:
    			begin += 1

    		begin +=1

    		while begin<m and list1[begin]==list2[begin-1]:
    			begin += 1

    		return begin>= m

    	# 下面是变化一个字符
    	if len(list1)-len(list2)==1 or len(list2)-len(list1)==1:
        # if abs(len(list1)-len(list2)==1):
    		if len(list1)-len(list2)>0:
    			return validDelAndInsert(list1,list2)
    		else:
    			return validDelAndInsert(list2,list1)

    	elif len(list1)==len(list2):
    		return validReplace(list1,list2)



if __name__ == "__main__":
	s1 = "horse"
	s2 = "ros"

	s = Solution()
	print(s.oneEditAway(s1, s2))

    



