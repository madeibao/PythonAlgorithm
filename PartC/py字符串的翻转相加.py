


while True:
    try:
        N, M = map(int, input().split())
    except:
        break
    def rev(x):
        return int(str(x)[::-1])

    print(rev(rev(N)+rev(M)))