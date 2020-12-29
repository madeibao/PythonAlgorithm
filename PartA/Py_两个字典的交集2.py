
a = {
    'x': 1,
    'y': 2,
    'z': 3,
    't': 4,
    'p': 5,
    'q': 6,
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
    't': 4,
    'p': 5,
    'q': 6,
}





bb = a.items() & b.items()
for k, v in bb:
    print(k, v)










