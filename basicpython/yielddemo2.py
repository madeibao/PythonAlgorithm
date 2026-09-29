

def fib(n:int):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count = count + 1

if __name__== "__main__":
    for num in fib(10):
        print(num, end=" ")

