1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 

则提问第n个数字是什么。


def getnum(n):
    for i in range(1, n+1):
        if ((i+1)*i)//2 >= n:
            return i


if __name__ == '__main__':
    num = int(input())
    print(getnum(num))

