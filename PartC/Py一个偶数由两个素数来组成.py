



def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def get(num):
    num2 = num//2
    list2 = []
    for j in range(num2, 0, -1):
        for i in range(num2, num):
            if isPrime(i) and isPrime(j) and i+j == num:
                list2.append(j)
                list2.append(i)

    print(list2[0])
    print(list2[1])


while True:
    try:
        num = int(input())
        get(num)
    except:
        break

