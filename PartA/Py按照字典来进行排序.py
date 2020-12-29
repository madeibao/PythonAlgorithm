


# # 其中的数字来按照字典的顺序来进行排序。

# 给定一个整数 n, 返回从 1 到 n 的字典顺序。

# 例如，

# 给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

# 请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lexicographical-numbers
# # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List

from collections import Counter

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
    	list2 = [i+1 for i in range(n)]

    	list3 = list(map(str, list2))
    	dic2 = Counter(list3)
    	sort = sorted(dic2.items(), key=lambda e: e[0])  

    	list4  = list(map(int, [i[0] for i in sort]))
    	return list4

if __name__ == "__main__":
	s = Solution()
	print(s.lexicalOrder(13))
