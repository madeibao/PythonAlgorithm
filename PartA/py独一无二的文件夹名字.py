
from typing import List
import Counter


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        dict2 = {}

        for name in names:
            base = name
            while name.count(name)>0:
                res.append(base+"("+str(dict2[base])+")")
                dict2[base]+=1
            dict2[name] = 1
        
        return res


if __name__ == "__main__":
    s = Solution()
    names = ["wano","wano","wano","wano"]
    print(s.getFolderNames(names))