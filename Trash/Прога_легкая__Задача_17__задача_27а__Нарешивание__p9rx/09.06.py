with open("15.txt") as f:
    a = [int(x) for x in f.readlines()]
    n = len(a)
k = 0
m = 1000000000000
for i in range(n-1):
    summa = a[i] + a[i+1]
    multi = a[i] * a[i+1]
    if summa % (multi//1000) == 0:
        k += 1
        m = min(m, a[i], a[i+1])
print(k, m)
