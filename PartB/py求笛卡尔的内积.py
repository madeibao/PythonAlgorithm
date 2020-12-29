

>>>import itertools
>>>m = 'ab'
>>>n = 'cd'
>#求m和n的笛卡尔积
>>>data = itertools.product(m,n)
>>>[x for x in data]
>[('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]
>#求m自身笛卡尔积
>>>data = itertools.product(m,m)
>>>[x for x in data]
>[('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]



