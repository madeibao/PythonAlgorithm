

import copy


origin = [1, 2, [3, 4]]

cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)   # 深拷贝和浅拷贝。


print(cop1 == cop2)   # true
print(coy1 is cop2)   # false
#cop1 和 cop2 看上去相同，但已不再是同一个object
origin[2][0] = "hey!"

print(origin)   #   [1, 2, ['hey!', 4]]
print(coy1)     #   [1, 2, ['hey!', 4]]
print(cop2)     #   [1, 2, ['hey!', 4]]


