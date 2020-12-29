 
# @param number string字符串 
# @return string字符串
#

# 逆置链表中的偶数的元素的值。
# 但是下面的算法的时间复杂度过大。

'''
class Solution:
    def change(self , number ):
        # write code here
        res = []
        list2 = list(map(int ,list(number)))
        for i in range(len(list2)):
        	if list2[i]%2==0:
        		res.append(list2[i])
        list3 = res[::-1]


        res3 = []

        for i in range(len(list2)):
        	if list2[i]%2==0:
        		res3.append(list3[0])
        		del list3[0]
        	else:
        		res3.append(list2[i])

        return "".join(list(map(str, res3)))

'''
#正则表达式。


import re
while True:
    try:
        a = input()
        length = len(a)
        ou = ['2','4','6','8']
        num = re.findall(r'([2468])',a)
        print(num)
        a = list(a)
        for i in range(length):
            if a[i] in ou:
                a[i] = num.pop()
        print(''.join(a))
    except:
        break

if __name__ == "__main__":
	s= Solution()
	str2 = "12346"
	print(s.change(str2))

