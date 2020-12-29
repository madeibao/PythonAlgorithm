
#----------------------------------------------------------------
9
cap
to
cat
card
two
too
up
boat
boot

# 输出：

boat
boot
cap
card
cat
to
too
two
up

#================================================================
#----------------------------------------------------------------



n = input()
a = []
for i in range(int(n)):
    a.append(input())
a.sort()
for i in range(int(n)):
    print(a[i],end = '\n')