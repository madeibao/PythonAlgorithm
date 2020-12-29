
import sys
arr=list(map(int,sys.stdin.readline().strip().split()))
sums=arr[0]+arr[1]
sums1=arr[0]+arr[2]
sums2=arr[1]+arr[2]
print(max(sums*arr[2],sums1*arr[1],sums2*arr[0],arr[1]*arr[0]*arr[2]))
    



a,b, c = list(map(int, input().split(" ")))
sum2 = a+b
sum3 = a+c
sum4 = b+c

print(max(sum2*a, sum))