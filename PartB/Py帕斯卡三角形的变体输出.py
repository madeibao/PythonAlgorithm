

# -*- coding: utf-8 -*-
           1

         1  1  1

      1  2  3  2  1

   1  3  6  7  6  3  1

1  4  10 16 19  16 10  4  1

以上三角形的数阵，
第一行只有一个数1，以下每行的每个数，是恰好是它上面的数，左上角数到右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。


def pascii(n):

	res= [[0]*(2*n-1) for i in range(n)]

	res[0][n-1]=1
	res[n-1][0]=1
	res[n-1][2*n-2]=1

	for i in range(1,n):
	    for j in range(1,2*n-2):
	        res[i][j]= res[i-1][j]+res[i-1][j-1]+res[i-1][j+1]

	temp = []
	for i in res:
		temp2  = []
		for j in i:
			if j!=0:
				temp2.append(j)
		temp.append(temp2)
	return temp


if __name__ == "__main__":
	n = int(input())
	print(pascii(n))