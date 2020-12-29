

# 并查集的思想。

import collections

def f3(hs, n):
    roots = {}
    res = collections.defaultdict(set)


    def findroot(node):

    	# 内部变量，引用外部节点的值。
        nonlocal roots

        if node not in roots:
            roots[node] = node
        elif roots[roots[node]] != roots[node]:
            roots[node] = findroot(roots[node])
        return roots[node]
    
    for h in hs:
        u, v = h
        
        if u not in roots:
            roots[u] = findroot(v)
        elif v not in roots:
            roots[v] = findroot(u)
        else:
            roots[findroot(u)] = findroot(v)
    
    for i in range(1, n + 1):
        curr = findroot(i)
        res[curr].add(i)
    ks = []
    
    for k in res:
        ks.append(sorted(res[k]))
    ks.sort(key = lambda k: k[0])
    return ks

while True:
    try:
        n, m = list(map(int, input().split()))
        hs = []
        for _ in range(m):
            temp = list(map(int, input().split()))
            hs.append(temp)
        ks = f(hs, n)
        print(len(ks))
        for k in ks:
            print(' '.join(map(str, k)))
    except:
        break





