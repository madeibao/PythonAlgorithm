# 比较两个版本的版本号的值。

from typing import List, Tuple

class Solution():
	def compareVersion(self,version1, version2):
		v1 = list(map(int ,version1.split(".")))
		v2 = list(map(int ,version2.split(".")))

		# 扩展成列表的长度。
		v1.extend([0]*(len(v2)-len(v1)))
		v2.extend([0]*(len(v1)-len(v2)))
		
		return 0 if v1==v2 else {True:1,False:-1}[v1>v2]



if __name__ == "__main__":
	s = Solution()
	str2 ="1.0.1"
	str3 ="1"
	print(s.compareVersion(str2,str3))

