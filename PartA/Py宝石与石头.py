

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        list1 = [i for i in J]
        list2 = [j for j in S]

        num = 0
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    num += 1
        return num


if __name__ == "__main__":
    s = Solution()
    J = "aA"
    S = "aAAbbbb"
    print(s.numJewelsInStones(J,S))
















