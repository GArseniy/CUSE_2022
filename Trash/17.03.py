s = """23
100
55
83
94
44
17
76
91
45
35
90
44
97
72
34
8
38
84
16"""

a = s.split()
b = [int(x) for x in a]
n = len(b)

count = 0
for i in range(n-1):
	for j in range(i+3, n):
		count += ((b[i] * b[j]) % 26 == 0)
print(count)
input()