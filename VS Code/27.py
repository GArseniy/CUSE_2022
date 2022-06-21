with open("fileB.txt") as f:
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]

min_pref = [10000000000]*10
min_pref[0] = 0

s = 0
ans = 0
for i in range(n):
    s += a[i]
    t = s%10
    if s - min_pref[t] > ans:
        ans = s - min_pref[t]
    if s < min_pref[t]:
        min_pref[t] = s
print(ans)
