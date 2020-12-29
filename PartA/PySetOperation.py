
s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

result = s | s2   # 这里是数学的运算的表达式。
print(result)  # 结果：{1, 2, 3, 4, 5, 6, 7}
print(s.union(s2))  # 两个集合的并运算。 {1, 2, 3, 4, 5, 6, 7}

result2 = s & s2   # 这里定义的是集合的交运算。

print(result2)      
result3 = s-s2	   # 定义集合的差集的运算。
result4 = s.difference(s2)  # 两个定义的结果是相同的。

print(result3)
print(result4)







"""

{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
{3, 4, 5}
{1, 2}
{1, 2}
"""