# 它的函数原型：string.strip(s[, chars])，它返回的是字符串的副本，并删除前导和后缀字符。
# （意思就是你想去掉字符串里面的哪些字符，那么你就把这些字符当参数传入。此函数只会删除头和尾的字符，中间的不会删除。）
# 如果strip()的参数为空，那么会默认删除字符串头和尾的空白字符(包括\n，\r，\t这些)。

a=" \rzha ng\n\t "
print(len(a))

b=a.strip()
print(b)
print(len(b))










# 11
# zha ng
# 6












