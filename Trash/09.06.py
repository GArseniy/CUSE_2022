def f(x, A):
    P = {2, 4, 6, 8, 10}
    Q = {3, 6, 9, 12, 15}
    return ((not (x in A)) <= (x in P)) or ((x in Q) <= (x in A))

A = set(range(2, 16))
for i in range(2, 16):
    B = A.copy()
    B.remove(i)
    if f(i, B):
        A = B.copy()
print(A)
print(len(A))


def f(x, a):  
    P = set([i * 2 for i in range(1, 6)])  
    Q = set([i * 3 for i in range(1, 6)])  
    return ((not(x in a)) <= (x in P)) or ((x in Q) <= (x in a))  
a = set()  
for x in range(20):  
    if not(f(x, a)):  
        a.add(x)
print(a)
print(len(a))
