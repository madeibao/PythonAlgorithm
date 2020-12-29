data = [
    {'age': 31, 'city': 'taipei', 'name': 'amy'},
    {'age': 71, 'city': 'tokyo', 'name': 'john'},
    {'age': 16, 'city': 'london', 'name': 'zoe'},
    {'age': 16, 'city': 'rio', 'name': 'cathy'},
    {'age': 48, 'city': 'frankfurt', 'name': 'david'}]


print(sorted(data, key=lambda x: x['age']))

# 按照年龄进行排序。
# 结果为：
# [{'age': 16, 'city': 'london', 'name': 'zoe'},
#  {'age': 16, 'city': 'rio', 'name': 'cathy'},
#  {'age': 31, 'city': 'taipei', 'name': 'amy'},
#  {'age': 48, 'city': 'frankfurt', 'name': 'david'},
#  {'age': 71, 'city': 'tokyo', 'name': 'john'}]




一样的效果
from operator import itemgetter
data = [
    {'age': 31, 'city': 'taipei', 'name': 'amy'},
    {'age': 71, 'city': 'tokyo', 'name': 'john'},
    {'age': 16, 'city': 'london', 'name': 'zoe'},
    {'age': 16, 'city': 'rio', 'name': 'cathy'},
    {'age': 48, 'city': 'frankfurt', 'name': 'david'}]
print(sorted(data, key=itemgetter('age')))


# [{'age': 16, 'city': 'london', 'name': 'zoe'},
#  {'age': 16, 'city': 'rio', 'name': 'cathy'},
#  {'age': 31, 'city': 'taipei', 'name': 'amy'},
#  {'age': 48, 'city': 'frankfurt', 'name': 'david'},
#  {'age': 71, 'city': 'tokyo', 'name': 'john'}]


