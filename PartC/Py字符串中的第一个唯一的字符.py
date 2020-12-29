


# 寻找字符串中的第一个唯一的字符内容。


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.Counter(s)
        for i, ch in enumerate(s):
            if dic[ch] == 1:
                return i
        return -1


if __name__ == "__main__":
	s =Solution()	
	print(s.firstUniqChar("leetcode"))

