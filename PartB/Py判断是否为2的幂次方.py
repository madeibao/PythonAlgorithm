


给定一个数字，
判断是否为2的幂指数。


可以通过2的幂指数的二进制的表示情况来判断

1    1
2    10
4    100
8    1000
16   10000

然后通过二进制的与运算  &


num = int(input())

if num&num-1==0:
	return True
else:
	return False

























