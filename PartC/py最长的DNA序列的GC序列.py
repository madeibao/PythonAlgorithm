


while True:
    try:
        line = input()
        limit = int(input())
        maxLine = ''
        maxPercent = 0.0
        for i in range(0, len(line) - limit + 1):  # head
            maxCount = 0
            for k in line[i:i + limit]:
                if k == 'C' or k == 'G':
                    maxCount += 1
            if maxPercent < 1.0 * maxCount / limit:
                maxPercent = 1.0 * maxCount / limit

                # 把字符串的结果值提取出来。
                maxLine = line[i:i + limit]
        print(maxLine)
    except:
        break
