


如果ABCD*9 = DCBA
求ABCD的值各自为多少。   1089


list2 = []

for A in range(1, 10):
    for B in range(10):
        for C in range(10):
            for D in range(10):
                if (A*1000 + B*100 + C*10+D)*9 == D*1000+C*100+B*10+A:
                    list2.append(A)
                    list2.append(B)
                    list2.append(C)
                    list2.append(D)

print(list2)









