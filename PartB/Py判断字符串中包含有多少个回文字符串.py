
while True:
    try:
        S = input()
        print(len(S))
        cnt = 0
        for i in range(len(S)):
            for j in range(i+1, len(S)+1):   # range函数前面是闭区间，后面是开区间。
                if(S[i:j]==S[i:j][::-1]):
                    cnt += 1
        print(cnt)
    except:
        break


一、字符串切片操作
切片 slice 操作可以让我们快速的提取子字符串。标准格式为：
[起始偏移量 start：终止偏移量 end：步长 step]  【步长step指：从某个索引开始往后数两位不包含该索引位】

操作和说明                        示例                            结果
[:]                               提取整个字符串                  "abcdef"[:]     "abcdef"
[start:]                          从start索引开始到结尾           "abcdef"[2:]    "cdef"
[::]                              从头开始到结尾                  "abcdef"[::]    "abcdef"
[:end]                            从头开始直到end-1               "abcdef"[:2]    "ab"
[start:end]                       从start到end-1                 "abcdef"[2:4]   "cd"
[start:end:step]                  从start提取到end-1，步长是step  "abcdef"[1:5:2] "bd"
【注：带有终止偏移量end的时候，采取包头不包尾的方式截取字符串】

 
注意力的是从尾部到头部的变化是从-1开始的。
其他操作（三个量为负数）的情况：
示例                            说明                                  结果
"abcdefghiwxyz"[-3:]            倒数三个                              "xyz"
"abcdefghij"[-8:-3]             倒数第八个到倒数第三个(包头不包尾)      "cdefg"
"abcdefghij"[::-1]              步长为负，从右到左反向提取              "jihgfedcba"

注：切片操作时，起始偏移量和终止偏移量不在[0,字符串长度-1]这个范围，也不会报错。
起始偏移量小于 0 则会当做 0，终止偏移量大于“长度-1”会被当成-1。
例如：
"abcdefg"[3:50]   结果："cdefg"

联系：
1. 将"to be or not to be"字符串倒序输出   "to be or not to be"[::-1]  结果：eb ot ton ro eb ot
2. 将"sxtsxtsxtsxtsxt"字符串中所有的s输出 "sxtsxtsxtsxtsxt"[::3] 结果：sssss









