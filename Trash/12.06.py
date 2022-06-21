from functools import lru_cache

def moves(h):
    a, b = h
    return [(a+1, b), (a, b+1), (a+2, b), (a, b+2), (a*2, b), (a, b*2)]

@lru_cache(None)
def game(h):
    if sum(h)>=47:
        return 0
    steps = [game(x) for x in moves(h)]
    if any(x%2 == 0 for x in steps):
        return 1 + min(x for x in steps if x%2 ==0)
    return 1 + max(steps)

for i in range(1, 40):
    print(i, game((7, i)))
