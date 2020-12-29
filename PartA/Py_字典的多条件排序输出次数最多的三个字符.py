给定一个字符串, 输出出现次数最多的前三个字符, 若两字符出现次数相同, 则按字典顺序排列.

# 样例输入

aabbbccde

# 样例输出

b 3
a 2
c 2


解法1：


from collections import Counter
c = Counter(input())   # 返回的是一个列表
l = sorted(c.items(), key=lambda s:(-s[1], s[0]))
for i in l[:3]:
    print(' '.join(map(str, list(i))))



解法2:

from collections import Counter
from operator import itemgetter

for item in (sorted(sorted(Counter(input()).items()), key=itemgetter(1), reverse=True)[:3]):
    print(str(item[0])+" "+str(item[1]))

解法3:
from collections import Counter

for letter, counts in sorted(Counter(input()).most_common(), key=lambda x:(-x[1],x[0]))[:3]:
    print(str(letter)+" "+str(counts))



解法4:
S = input()
letters = [0]*26

for letter in S:
    letters[ord(letter)-ord('a')] += 1

for _ in range(3):

    max_letter = max(letters)

    for index in range(26):
        if max_letter == letters[index]:
            print(str(chr(ord('a')+index))+" "+str(max_letter))
            letters[index] = -1
            break




            
a, b= map(int, input().split(" "))

dict2 ={}
for i in range(a):
	x, y = map(int, input().split(" "))
	dict2[x]+=y

l = sorted(dict2.items(), key=lambda s:(-s[1], s[0]))