

from itertools import permutations

string = list(input())

string.sort()

for item in permutations(string):
    item = ''.join(item)
    print(item)

print('')

# abc

# 输出结果:

abc
acb
bac
bca
cab
cba
