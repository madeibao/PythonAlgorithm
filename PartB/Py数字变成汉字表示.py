

def numberToWords(num):
    to19='one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen seventeen eighteen nineteen'.split()
    tens="twenty thirty forty fifty sixty seventy eighty ninety".split()
    def words(n):
        if n<20:return to19[n-1:n]
        if n<100:return [tens[n//10-2]]+words(n%10)
        if n<1000:
            return [to19[n//100-1]]+["hundred"]+["and"]+words(n%100)
        for p,w in enumerate(('thousand',"million","billion"),1):
            if n<1000**(p+1):
                return words(n//1000**p)+[w]+words(n%1000**p)
    return " ".join(words(num)) or "Zero"
while True:
    try:
        print(numberToWords(int(input())))
    except:break