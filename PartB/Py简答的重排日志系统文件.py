

# 简单的重排日志系统
#你有一个日志数组 logs。每条日志都是以空格分隔的字串。
'''
对于每条日志，其第一个字为字母与数字混合的 标识符。

除标识符之外，所有字均由小写字母组成的，称为 字母日志
除标识符之外，所有字均由数字组成的，称为 数字日志
题目所用数据保证每个日志在其标识符后面至少有一个字。

请按下述规则将日志重新排序：

所有 字母日志 都排在 数字日志 之前。
字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序；
数字日志 应该按原来的顺序排列。
返回日志的最终顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-data-in-log-files
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# =================================================================
# =================================================================


# 数字日志按照原来的内容来进行排序。



from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

    	# 这里存储的是字母的日志
    	alphaLog = []
    	# 这里存储的是数字的日志。
    	numLog = []

    	for i in logs:
    		if self.isAlpha(i):
    			alphaLog.append(i)
    		else:
    			numLog.append(i)

    	res = []
    	res = self.specialSort(alphaLog)
    	res += numLog
    	return res 

    	
    def isAlpha(self, strs):
	    list2 = strs.split(" ")
	    res = list(list2[1])
	    for i in range(len(res)):
	        if not (ord(res[i])<=57 and ord(res[i])>=48):
	            return True
	    return False

    def specialSort(self, list2):
        temp = []

        for i in list2:
            index = i.index(" ")
            a = i[:index]
            b = i[index+1:]
            temp.append((a, b))

        temp.sort(key=lambda elem: (elem[1], elem[0]))
        res = []
        for i in temp:
            res.append(" ".join(i))
        return res


if 	__name__ == "__main__":
	s = Solution()
	list2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
	print(s.reorderLogFiles(list2))

