

#字符串的压缩的形式
# aaabbbcccddd 


str2 = input().strip()
cnt = 1
res = "" 
for i in range(1, len(str2)):
	if str2[i]==str2[i-1]:
		cnt+=1
	else:
		res+=str(cnt)+str2[i-1]
		cnt =1
res+=str(cnt)+str2[-1]

print(res)

