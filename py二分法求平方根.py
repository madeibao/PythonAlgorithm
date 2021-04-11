

# 通过二分法来求平方根。


x=float(input('Enter the number:'))
low=0.0
high=x
guess=(low+high)/2
while abs(guess**2-x)>1e-4:
    if guess**2>x:
        high=guess
    else:
        low=guess
    guess=(low+high)/2
 
print(guess)





