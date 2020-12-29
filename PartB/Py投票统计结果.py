

import sys

try:
    while True:
        n = sys.stdin.readline()
        line1 = sys.stdin.readline().strip().split()
        if not line1:
            break
        candi = dict.fromkeys(line1, 0)
        print(candi)
        invalid = []
        n = sys.stdin.readline()
        vote = sys.stdin.readline().strip().split()
        for s in vote:
            if s in candi:
                candi[s] += 1
            else:
                invalid.append(s)
        # output
        for item in line1:
            print('%s : %s' % (item, candi[item]))
        print('Invalid :',  len(invalid))
except:
    pass