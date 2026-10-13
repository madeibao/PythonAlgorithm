

def add(x, lst=[]):
    lst.append(x)
    return lst

if __name__ == "__main__":
    print(add(1))
    print(add(2, []))
    print(add(3))

# 输出结果如下:
'''

函数默认列表对象A：一开始 []
add(1) → 对象A: [1]
add(2, []) → 新建对象B：[2]，对象A不变
add(3) → 对象A继续追加 → [1,3]


[1]
[2]
[1, 3]

'''
