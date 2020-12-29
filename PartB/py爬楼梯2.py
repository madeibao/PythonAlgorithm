


class Solution():
    def climstairs(self,n):
        a , b= 1, 1

        for i in range(2, n+1):
            temp = a+b
            b = a
            a = temp
        return b


if __name__ == "__main__":
    s= Solution()
    n =3
    print(s.climstairs(n))

