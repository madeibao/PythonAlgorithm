


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIndex = {s:i for i, s in enumerate(S)}
        startTemp = 0
        j = 0
        ret = []
        for i, s in enumerate(S):
            j = max(lastIndex[s], j)
            if i == j:
                ret.append(j - startTemp + 1)
                startTemp = j + 1 # 下一段的左端一定是当前结尾的右端＋1
        return ret


if __name__ == "__main__": 
	s = Solution()
	print(s.partitionLabels("abccaddbeffe"))



