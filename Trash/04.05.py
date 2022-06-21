n = int(input())
numbers = [int(input()) for i in range(n)]
max_len = 0
ans = 0
for i in range(n):
    for j in range(i+1, n):
        c = []
        for k in range(i, j+1):
            if k % 2 == numbers[i] % 2:
                c.append(numbers[k])
        if sum(c) % 12 == 0:
            if len(c) >= max_len:
                max_len = len(c)
                ans = sum(c)
print(ans)
