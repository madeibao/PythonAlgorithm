
# # 字符串的压缩
# aaaabbbb
# 3a3b


# aaabbbdd
# 2a2b1d

#----------------------------------------------------------------

s=input()
ans=[]
cnt=0
for i in s:

    # 第一个字符
    if not ans:
        ans.append(i)
        continue
    if i !=ans[-1]:
        if cnt:
            ans.insert(-1,cnt)

        # 计数单位重新的置零。
        cnt=0
        ans.append(i)
    else:
        cnt+=1

if cnt:
    ans.insert(-1,cnt)
print(''.join(list(map(str,ans))))


# 第二种情况的字符串压缩算法
# 两种情况不一样的结果。

#对字符串进行RLE压缩，将相邻的相同字符，用计数值和字符值来代替。例如：aaabccccccddeee，则可用3a1b6c2d3e来代替。

#输入描述:
#输入为a-z,A-Z的字符串，且字符串不为空，如aaabccccccddeee
#输出描述:
#压缩后的字符串，如3a1b6c2d3e

#----------------------------------------------------------------

import sys

if __name__ == "__main__":
    s = input().strip()
    count = 1
    ans = ""
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            ans += str(count) + s[i - 1]
            count = 1
    ans += str(count) + s[-1]
    print(ans)



#--------------------------------------

# 字符串的压缩的算法

if __name__ == '__main__':
    s = input()
    s = s.strip()
    count =1

    ans=""
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            count +=1
        else:
            ans += str(count) + s[i-1]
            # 重新的置1
            count =1
    ans += str(count) + s[-1]

    print(ans)












