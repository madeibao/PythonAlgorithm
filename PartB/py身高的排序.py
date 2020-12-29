


# --*-- coding : utf-8 --*--
def No1(k, ls):
    if k == 0: return []
 
    res = [-1]
    if k == 1: return res
    res = []
    for i in range(k-1):
        temp = ls[i + 1:]
 
        #print(temp)
        #print(ls[i + 1:])
 
        if max(temp) <= ls[i]:
            res.append(-1)
        else:
            for j in temp:
                if j > ls[i]:
                    res.append(j)
                    break
    res.append(-1)               
    return res
 
 
if __name__ == '__main__':
 
    n = input()
    n = int(n)
 
    m = input().split(' ')
    m = list(map(int, m))
    m = list(reversed(m))
    #print(m)
    res1 = list(reversed(No1(n, m)))
    print(n)
    print(' '.join([str(x) for x in res1]))