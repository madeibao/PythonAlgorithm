

import itertools

str2 = "aaaba"

for _, j in itertools.groupby(str2):
    print(list(j))
    
    

# ==========----------------------------------------------------------------=

['a', 'a', 'a']
['b']
['a']

# ==========----------------------------------------------------------------=

