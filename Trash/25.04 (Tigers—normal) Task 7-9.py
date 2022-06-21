from functools import lru_cache


def moves(h):
    return h+2, h*3


@lru_cache(None)
def f(h):
    if 45 <= h <= 112:
        return "END"
    if h > 112:
        return "BAD_END"
    if any(f(x) == "END" for x in moves(h)):
        return "WIN1 (за 1 игровой ход)"
    if any(all(f(y) == "BAD_END" for y in moves(x)) and f(x) != "BAD_END" for x in moves(h)):
        return "WIN1 (за 2 игровых хода)"
    if any(f(x) == "END" or all(f(y) == "BAD_END" for y in moves(x)) and f(x) != "BAD_END" for x in moves(h)):
        return "WIN1 (за 1 или 2 игровых хода)"
    if all(f(x) == "WIN1" for x in moves(h)):
        return "LOSE1 (за 2 игровых хода)"
    if all(f(x) == "BAD_END" for x in moves(h)):
        return "LOSE1 (за 1 игровой ход)"

    if any(f(x) == "LOSE1" for x in moves(h)):
        return "WIN2"
    if any(f(x) == "LOSE1 (BAD_END)" for x in moves(h)):
        return "WIN1 or WIN2"
    if all(f(x) == "WIN1" or f(x) == "WIN2" for x in moves(h)):
        return "LOSE2"
    if all(f(x) == "WIN1 or WIN2" for x in moves(h)):
        return "LOSE2"

# TODO: don't work

for i in range(1, 45):
    print(i, f(i))
