
# This is a simple Python script to find the minimum and maximum values in a list of numbers.
# float('inf') is used to initialize minNum to positive infinity, ensuring that any number in the list will be smaller.
# float('-inf') is used to initialize maxNum to negative infinity, ensuring that any number in the list will be larger.

minNum = float('inf')

maxNum = float('-inf')

res = [1,2,3,4,5]

for num in res:
    if num < minNum:
        minNum = num
    if num > maxNum:
        maxNum = num

print("最小值:", minNum)
print("最大值:", maxNum)



