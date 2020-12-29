

while True:
    try:

        num = list(map(int ,input().split(",")))
        n = len(nums)
        print(int((n+0)*(n+1)/2 - sum(nums)))
    except:
        break



        