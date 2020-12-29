
1. 省略start和end参数时

print("MacBook Pro".find("Pro"))  # 8
print("MacBook Pro".find("Pro ")) # -1      注意字符串中有空格。


2. 仅使用start参数
当使用start参数时，表示字符串第start个参数开始寻找sub字符串，并返回结果。


print("MacBook Pro".find("Pro", 1))  # 8
print("MacBook Pro".find("Pro", 9))  # -1


3. 同时使用start和end
同时使用start和end时，find方法将在字符串第start字符开始，第end-1个字符结束的子串中查找sub字符串，并返回结果。

print("MacBook Pro".find("Pro", 1, 11))  #  8
print("MacBook Pro".find("Pro", 1, 3))   #  -1





注意事项

1. start参数和end参数可以是负整数

start和end可以是负整数，表示对字符串反向查找。

>>> "MacBook Pro".find("o", -1)   10



>>> "MacBook Pro".find("o", 1)   4

 

2. 当要比对的参数sub不存在字符串str中时，find()方法返回-1.

>>> "MacBook Pro".find("Apple")-1

 

3. start和end超出实际的字符串范围时，find()方法不会报错

>>> "MacBook Pro".find("o", -99)4>>> "MacBook Pro".find("o", 999, -1)






























