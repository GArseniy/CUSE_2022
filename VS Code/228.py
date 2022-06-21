k = 0
for x1 in "0123456789": #TODO: проверить 0
    for x2 in "0123456789":
        for i in range(100000):
            x3 = str(i)
            n = x1 + "3579" + x2 + "6" + x3
            n = int(n)
            if n < 10**9:
                if n % 7 ==0:
                    k += 1
print(k)
