

https://blog.csdn.net/weixin_43978812/article/details/90666160





str1 = input()  #让用户输入字符串1
str2 = input()  #让用户输入字符串2
list2 = []      #空列表
for i in range(len(str1)):
    if str1[i:i+len(str2)] == str2:
        list2.append(i)
print(len(list2))


# abcdabcab
# ab
# 3
