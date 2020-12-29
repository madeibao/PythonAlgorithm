

sx = 'abcd'
sy = 'abcdabab'
#找出较短的字符串
if len(sx) > len(sy):
    str1 = sy
    str2 = sx
else:
    str1 = sx
    str2 = sy
#str1 为较短的字符串   
max = 0
for i in range(len(str1),0,-1):    #字符串长度：从大到小，则第一个相同的，则为最大公共字符串，#较大程度减少算法复杂度
    for j in range(len(str1)+1-i):  #难度：j 的取值范围： len(str1)+1-i ，详细解释见思路分析 
        if str1[j:j+i] in  str2:
            max = i
            chuan = str1[j:j+i]
            break
    if max >0:
        break

        
if max > 0:
    print('最大公共子串的字符数为：%i'%max)
    print('最大公共子串为：%s'%chuan)
else:
    print('不存在最大公共子串')
