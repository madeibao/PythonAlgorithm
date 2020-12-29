
def byte_size(string):
    return (len(string.encode('utf-8')))


print(byte_size('😀'))  # 4

print(byte_size('Hello World'))  # 11





