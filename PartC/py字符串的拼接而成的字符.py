
# 一个字符串是否由其他的字符拼接而成。
'''
题目描述
给出一个非空的字符串，判断这个字符串是否是由它的一个子串进行多次首尾拼接构成的。
例如，"abcabcabc"满足条件，因为它是由"abc"首尾拼接而成的，而"abcab"则不满足条件。
输入描述:
非空字符串
输出描述:
如果字符串满足上述条件，则输出最长的满足条件的的子串；如果不满足条件，则输出false。
示例1
输入
复制
abcabc
输出
复制
abc

'''

while True:
    try:
        string = input()
        stringLen = len(string)
        whether = 'false'

        # 如果字符串的长度小于3的话，
        if stringLen<3:
            if string.count(string[0])==stringLen:
                whether = string[0]
        else:
            for i in range(stringLen//2+1,0,-1):
                if string.count(string[:i])*i==stringLen:
                    whether = string[:i]
                    break
        print(whether)
    except Exception:
        break









