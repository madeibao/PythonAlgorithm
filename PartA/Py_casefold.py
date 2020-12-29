# !/usr/bin/python3
 


#  Python casefold() 方法是Python3.3版本之后引入的，其效果和 lower() 方法非常相似，都可以转换字符串中所有大写字符为小写。
# 两者的区别是：lower() 方法只对ASCII编码，也就是‘A-Z’有效，对于其他语言（非汉语或英文）中把大写转换为小写的情况只能用 casefold() 方法。
# 封装了非汉语的方法来实现对字符的小写的转变。


S1 = "Runoob EXAMPLE....WOW!!!" #  英文
S2 = "ß"  #德语
 
print(S1.lower())
print(S1.casefold())
print(S2.lower())
print(S2.casefold()) 	

#  德语的"ß"正确的小写是"ss"








