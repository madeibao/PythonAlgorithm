# python中的chr(i)函数

# 返回整数i对应的ASCII字符。与ord()作用相反。

# 参数x：取值范围[0, 255]之间的正数。
# 版本：该函数在python2和python3各个版本中都可用。不存在兼容性问题。
# 例子：

chr() 函数映射数字来对应的ASCII 码的值
ord() 函数映射ASCII的内容来变成数字。
     # * 阿斯玛的基本的范围
     #     *
     #     * 数字 :48-57
     #     *      0 -- 48
     #     *      9 -- 57
     #     *
     #     * 大写字母:65-90
     #     *  A -- 65
     #     *  Z -- 90
     #     *
     #     * 小写字母:97-122
     #     * a -- 97
     #     * z -- 122
     #  大小写字母的差值为32.

chars= [102,108,97,103,123,49,51,50,17,56,117,55,121,51,49,114,55,56,101,117,49,101,50,125]

chars2 = sorted(chars)
for char in chars2:
	print(chr(char), end='')


print("\n")
print("----------------------------------------------------------------")
chars = ['a', 'b']




for char in chars:
    print(ord(char))











                                              