import itertools
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        list2 = []
        for i in time:
            list2.append(i%60)
        
        dict2 = {}
        count = 0
        for item in list2:
            if item in dict2:
                count += dict2[item]

            if item==0:
                if item in dict2:
                    dict2[0]+=1
                else:
                    dict2[0]=1
            elif item!=0:
                if item in dict2:
                    dict2[item] += 1
                else:
                    dict2[item] = 1
        return count

if __name__=='__main__':
    s = Solution()
    print(s.numPairsDivisibleBy60([30,20,150,100,40]))