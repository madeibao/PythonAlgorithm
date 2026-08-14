"""
题目：字符串每k个一组来进行翻转
"""
def demo(s):
    temp = []
    for i in range(0, len(s), 3):
        temp.append(s[i:i+3])
    return "".join([i[::-1] for i in temp])

old_str = "12345678"
print(demo(old_str))

