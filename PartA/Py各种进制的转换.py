
Python的各种进制的转换

16进制的打印
例如10进制的36和10


print(hex(10))
print(hex(36))


0xa
0x24
#-----------------------------------------------------------------

8进制的打印

print(oct(10))

0o12
#-----------------------------------------------------------------

2进制的打印结果：

print(bin(15))

0b1111


# 打印结果值。
#------------------------------	----------------------------------
a = 36

print("0x%x"%(a))
print("0o%o"%(a))
print(bin(a))

# format的格式的打印结果值。

print('{:b}'.format(17))   # 二进制打印   10001
print('{:d}'.format(17))   # 十进制打印   17
print('{:o}'.format(17))   # 八进制打印   21
print('{:x}'.format(17))   # 16进制打印   11





