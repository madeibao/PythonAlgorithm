


str2 = list(input())
set2 = set(str2)

res = ""
for i in str2[::-1]:
	if i not in res:
		res += i

print(int(res))