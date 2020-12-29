






x = 3
case = 'b'
result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2,
}

m = result['b'](x)
print(m)   #  结果10











