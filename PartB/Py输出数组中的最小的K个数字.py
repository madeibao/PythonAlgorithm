# 5 2
# 1 3 5 7 2


while True:
    try:
        count = int(input().split(" ")[1])
        array = list(map(int, input().strip().split(" ")))
        print(" ".join(map(str, sorted(array)[:count])))
    except:
        break














