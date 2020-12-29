import math
class Fc:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c

	def jie(self):
		if(self.a==0):
			if(self.b==0):
				return "-1"
		return 'x={:.2f}'.format((-self.c)/(self.b))
		delta = self.b**2-4*self.a*self.c
		if(delta>0):
			x1=(-self.b- math.sqrt(delta))/(2*self.a)
			x2=(-self.b+ math.sqrt(delta))/(2*self.a)
			return 'x1={:.2f},x2={:.2f}'.format(x1,x2)
		elif(delta==0):
			return 'x={:.2f}'.format((-self.b)/(2*self.a))
		else:
			return '-1'


if __name__ == '__main__':
    m=int(input())
    for i in range(m):
        xs=list(map(int,input().split()))
        fc=Fc(xs[0],xs[1],xs[2])
        print(fc.jie())

