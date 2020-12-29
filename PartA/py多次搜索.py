

from typing import List
class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        result=[]
        for i in smalls:
            if i=='':
                result.append([])
                continue
            if i not in big:
                result.append([])
            else:
                record=[]
                length=len(i)
                j=0
                # 注意的是python中都是从0开始进行记录位置的。
                while j+length-1<len(big):
                    if i==big[j:j+length]:

                        # 记录初始的位置j
                        record.append(j)
                    j+=1    
                result.append(record)
        return result





if __name__ == "__main__":
    s =Solution()
    big = "mississippi"
    smalls = ["is","ppi","hi","sis","i","ssippi"]
    print(s.multiSearch(big,smalls))