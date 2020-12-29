
#------------------------------------------------------------------


class Solution:

    def numJewelsInStones(self, J: str, S: str) -> int:
        res = [x for x in S if x in J]  # S中在J中出现的元素；同理可以延伸S中不在J中出现的元素
        return len(res)


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    s2 = Solution()
    print(s2.numJewelsInStones(J, S))

