from functools import lru_cache


def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)


@lru_cache(None)
def f(h):
    if sum(h) >= 55:
        return "END"
    if any(f(x) == "END" for x in moves(h)):
        return "WIN1"
    if all(f(x) == "WIN1" for x in moves(h)):
        return "LOSE1"
    if any(f(x) == "LOSE1" for x in moves(h)):
        return "WIN2"
    if all(f(x) == "WIN1" or f(x) == "WIN2" for x in moves(h)):
        return "LOSE2"


for i in range(1, 45):
    if f((10, i)) == "LOSE2":
        print(i, f((10, i)))
