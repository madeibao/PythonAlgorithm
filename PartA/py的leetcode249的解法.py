
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

import collections


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        record = collections.defaultdict(list)
        for i, word in enumerate(strings):
            tmp = tuple()
            for j in range(1, len(word)):
                num = ord(word[j]) - ord(word[j - 1])
                if num < 0:
                    num += 26
                tmp += (j, num)
            record[tmp].append(word)
        
        print(dict(record))
        return list(record.values())

if __name__ == "__main__":
	s =Solution()
	list2 = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
	print(s.groupStrings(list2))

