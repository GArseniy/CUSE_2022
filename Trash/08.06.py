for i in range(1, 100000000000):
    x = i
    a = 0
    b =1
    while x > 0:
        a += 1
        b *= x%100
        x //= 100
    if a == 4 and b == 4586868:
        print(i)
        
