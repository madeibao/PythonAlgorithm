


class Solution():
    def legal(self,str2):
        ip = list(map(int,str2.split(".")))

        if len(ip)!=4:
            return False
        
        for i in range(len(ip)):
            if ip[i]>255 or ip[i]<0:
                return False
        return True



if __name__=='__main__':
    s = Solution()
    print(s.legal("255.23.23.23"))


    