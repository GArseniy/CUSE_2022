from functools import lru_cache


def moves(h):
    if h%2 == 0:
        return h+1, h+3
    return [h*3]


@lru_cache(None)
def f(h):
    if h >= 51:
        return "END"
    if any(f(x) == "END" for x in moves(h)):
        return "WIN1"
    if all(f(x) == "WIN1" for x in moves(h)):
        return "LOSE1"
    if any(f(x) == "LOSE1" for x in moves(h)):
        return "WIN2"
    if all(f(x) == "WIN1" or f(x) == "WIN2" for x in moves(h)):
        return "LOSE2"


count = 0
for i in range(1, 51):
    if f(i) == "LOSE2":
        print(i, f(i))
        count += 1
print(count)
