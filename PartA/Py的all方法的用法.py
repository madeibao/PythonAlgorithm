

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True



>>> all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
True
>>> all(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
False
>>> all([0, 1，2, 3])          # 列表list，存在一个为0的元素
False
   
>>> all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
True
>>> all(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
False
>>> all((0, 1, 2, 3))          # 元组tuple，存在一个为0的元素
False
   
>>> all([])             # 空列表
True
>>> all(())             # 空元组
True