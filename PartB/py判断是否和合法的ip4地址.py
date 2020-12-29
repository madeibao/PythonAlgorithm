
# 判断是否为合法的IP4 地址的值。


class Solution():
    def legal(self,str2):
        ip = list(map(int,str2.split(".")))
        if len(ip)!=4:
            return False
        for i in range(len(ip)):
            if ip[i]>255 or ip[i]<0:
                return False
        return True


if __name__=="__main__":
    s =Solution()
    str2 = "255.223.22.255"
    print(s.legal(str2))