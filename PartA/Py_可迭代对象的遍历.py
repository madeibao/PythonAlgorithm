

def sum(items):
    head, *tail = items
    print(head, tail)
    return head+sum(tail) if tail else head


items = [1, 2, 3, 4, 5, 6]
sum(items)


# 1 [2, 3, 4, 5, 6]
# 2 [3, 4, 5, 6]
# 3 [4, 5, 6]
# 4 [5, 6]
# 5 [6]
# 6 []



