# -*- coding: utf-8 -*-


class Solution():
    def compressString(self,str2):
        count = 1

        list2 = list(str2)
        res = ""
        for i in range(1, len(list2)):
            if list2[i]==list2[i-1]:
                count += 1
            else:
                res += str(count) +list2[i-1]
                count = 1
        
        res += str(count) + list2[-1]
        return res

if __name__ == '__main__': 
    s = Solution()
    print(s.compressString("aaabbbcccddd"))

    

            
