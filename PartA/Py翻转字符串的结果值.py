
# 一个字符串的句子结果进行整体的翻转来得到最终的结果值。


class Solution(object):
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])


if __name__ == '__main__': 
	s = Solution()
	print(s.reverseWords("the sky is blue"))