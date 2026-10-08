

import copy

res = [1,2,2,3]

res2 = copy.deepcopy(res)

res.append(4)

print(res)
print(res2)