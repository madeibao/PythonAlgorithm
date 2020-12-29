

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            2:['a', 'b', 'c'],
            3:['d', 'e', 'f'],
            4:['g', 'h', 'i'],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r','s'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y','z'],
        }

        if len(digits)==0: return []
        if len(digits)==1: return dic[int(digits[0])]

        list2 = []
        result = self.letterCombinations(digits[1:])

        for i in result:
            for j in dic[int(digits[0])]:
                list2.append(j+i)
        return list2


if __name__ == "__main__":
	s = Solution()
	list2 ="23"
	print(s.letterCombinations(list2))

