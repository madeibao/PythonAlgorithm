



def get_multiplier(a):
    def out(b):
         return a * b
    return out


cc = get_multiplier(10)
print(cc(10))








