a = 544
s = ""
while a > 0:
    s = str(a%3) + s
    a //= 3
print(s)

name = input()
print(name)
input()