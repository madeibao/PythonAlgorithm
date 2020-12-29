


while True:
    try:
        string = input()
        dictionary = {}
        for i in range(len(string)):
            if string[i] not in dictionary:
                dictionary[string[i]] = 1
            else:
                dictionary[string[i]] += 1
        x = []
        for j in dictionary:
            x.append(dictionary[j])


        x.sort()
        sum_line = 0
        while len(x) >= 2:
            x[1] += x[0]
            sum_line += x[1]
            x.pop(0)
            x.sort()
        print(sum_line)
    except:
        break








