
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

# 示例 1:

# 输入: "hello"
# 输出: "holle"
# 示例 2:

# 输入: "leetcode"
# 输出: "leotcede"


class Solution:
    def reverseVowels(self, s: str) -> str:

    	left = 0
    	right = len(s)-1

    	list2 = list(s)
    	while True:
    		if left >right:
    			break

    		# 只要不是在元音的字符内的字符，都将逐渐的移动。
    		while left < right and list2[left] not in 'aeiouAEIOU':
    			left += 1
    		while left < right and list2[right] not in 'aeiouAEIOU':
    			right -= 1

    		# 两个位置的字符来进行交换。
    		list2[left], list2[right] = list2[right], list2[left]

    		left += 1 
    		right -= 1 

    	return "".join(list2)


if __name__ == "__main__":
	s = Solution()
	print(s.reverseVowels("leetcode"))




    	






