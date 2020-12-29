Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串，仅针对字符串的方法。

split() 方法语法：

str.split(str="", num=string.count(str)).
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。
返回分割后的字符串列表。

# 返回的是分割后的字符串的列表。



>>> s = 'love you aa a ! a'
>>> s.split()
['love', 'you', 'aa', 'a', '!', 'a']
>>> s.split(',')
['love you aa a ! a']
>>> s.split('!')
['love you aa a ', ' a']





