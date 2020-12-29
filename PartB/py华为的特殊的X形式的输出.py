

EVERYTHINGGOESWELL,5 => EIWETGELYORHGSLVNE

['E', 'V', 'E', 'R', 'Y', 'T', 'H', 'I', 'N', 'G', 'G', 'O', 'E', 'S', 'W', 'E', 'L', 'L']
E       V
  E   R
    Y
  T   H
I       N
  G   G
    O 
  E   S
W       E
  L   L


# ------------------------------------------------------------------------------
EVERYTHINGGOESWELL,3 => ERHGEEETNOWLVYIGSL

E   V
  E
R   Y
  T
H   I
  N  
G   G
  O
E   S
  W
E   L
  L



#------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

def computeCol(n, i):
    if i < n:
        if i % 2 == 0:
            return i // 2
        return n - 1 - (i // 2)
    else:
        center = n // 2
        offset = (i - n) // 2 + 1
        if i % 2 != 0:
            return center - offset
        return center + offset

def run():
    string, length = input().split(',')
    length = int(length)
    result = [[] for _ in range(length)]
    for i, val in enumerate(string):
        result[computeCol(length, i % (2 * length - 3))].append(val)
    for i in result:
        for j in i:
            print(j, end = '')
    print('')


if __name__ == '__main__':
    run()
