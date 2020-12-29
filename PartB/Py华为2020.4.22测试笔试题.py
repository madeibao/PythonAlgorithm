


a,b = input().split(",")
list2 = list(a)


# 3d50J,Aa3
#----
#----------------------------------------------------------------
#-----------------------------------------------------------------

m = input()
list2 = list(m)
res = ""

for i in range(len(list2)):
	if ord(list2[i])>=48 and ord(list2[i])<=57:
		res += str(list2[i])

res = sorted(list(res))
print("".join(res))

