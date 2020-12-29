# 说明：
# 在传入参数时通过“参数名:类型”的形式声明参数的类型；
# 返回结果通过"-> 结果类型"的形式声明结果的类型。
# 在调用的时候如果参数的类型不正确pycharm会有提醒，但不会影响程序的运行。
# 对于如list列表等，还可以规定得更加具体一些，如：“-> List[str]”,规定返回的是列表，并且元素是字符串。
# 由于python天生支持多态，迭代器中的元素可能多种，如下：




from typing import List, Tuple, Dict

def add(a:int, string:str, f:float, b:bool) -> Tuple[List, Tuple, Dict, bool]:

    list1 = list(range(a))

    tup = (string, string, string)

    d = {"a":f}

    bl = b

    return list1, tup, d,bl

print(add(5,"hhhh", 2.3, False))

# 结果：([0, 1, 2, 3, 4], ('hhhh', 'hhhh', 'hhhh'), {'a': 2.3}, False)


#------------------------------------------------------------------------------

from typing import List, Tuple, Dict

def func(a: int, string: str) -> List[int or str]:

    list1 = []
    list1.append(a)
    list1.append(string)
    return list1

# 使用or关键字表示多种类型


print(func(3, "abc"))


# [3, 'abc']






