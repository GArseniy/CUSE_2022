from functools import lru_cache


def moves(h):
    a, b, c = h
    if a <= 1:
        if b <= 1:
            if c <= 1:
                return BrokenPipeError
            else: return (a, b, c - 1), (a, b, c//2 + c%2)
        else:
            if c <= 1:
                return (a, b-1, c), (a, b//2 + b%2, c)
            else: return (a, b-1, c), (a, b//2 + b%2, c), (a, b, c - 1), (a, b, c//2 + c%2)
    else:
        if b <= 1:
            if c <= 1:
                return (a-1, b, c), (a//2 + a%2, b, c)
            else:
                return (a-1, b, c), (a//2 + a%2, b, c), (a, b, c - 1), (a, b, c // 2 + c % 2)
        else:
            if c <= 1:
                return (a-1, b, c), (a//2 + a%2, b, c), (a, b - 1, c), (a, b // 2 + b % 2, c)
            else:
                return (a-1, b, c), (a//2 + a%2, b, c), (a, b - 1, c), (a, b // 2 + b % 2, c), (a, b, c - 1), (a, b, c // 2 + c % 2)


@lru_cache(None)
def f(h):
    if sum(h) <= 32:
        return "END"
    if any(f(x) == "END" for x in moves(h)):
        return "WIN1"
    if all(f(x) == "WIN1" for x in moves(h)):
        return "LOSE1"
    if any(f(x) == "LOSE1" for x in moves(h)):
        return "WIN2"
    if all(f(x) == "WIN1" or f(x) == "WIN2" for x in moves(h)):
        return "LOSE2"


for i in range(12, 101):
    print(i, f((11, 11, i)))
