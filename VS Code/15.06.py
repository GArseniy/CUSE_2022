s = "6024 5008 3531 343 1658 5228 9997 833 3592"
a = s.split()
b = [int(x) for x in a]
b.sort()
for x in b:
    print(x, end=" ")
