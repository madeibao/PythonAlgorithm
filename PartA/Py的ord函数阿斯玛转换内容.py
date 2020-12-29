ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常


>>>ord('a')
97
>>> ord('b')
98
>>> ord('c')
99


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


chr()函数
i -- 可以是 10 进制也可以是 16 进制的形式的数字，数字范围为 0 到 1,114,111 (16 进制为0x10FFFF)。

>>>chr(0x30)
'0'
>>> chr(97) 
'a'
>>> chr(8364)
'€'











