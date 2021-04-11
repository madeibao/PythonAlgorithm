

from itertools import permutations

def functool(str):
    res = []
    for i in permutations(str):
        res.append("".join(i))
    return res


print(len(set(functool("aab"))))









