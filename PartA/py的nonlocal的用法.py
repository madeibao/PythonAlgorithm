





def fun2():
	count = 0
	def fun3():
		nonlocal count
		count += 1
		return count
	return fun3

val = fun2()
print(val())