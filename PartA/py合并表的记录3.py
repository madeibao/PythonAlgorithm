

n = int(input())
dict2 = {}

for i in range(n):
    a,b = map(int, input().split(" "))
    if a not in dict2.keys():
        dict2[a] = b
    else:
        dict2[a] +=b 


for key, value in dict2.items():
    print(str(key) + " "+str(value))

    
