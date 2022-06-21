from functools import lru_cache
@lru_cache(None)
def game(h): return (h<50)*(1 + (any(x % 2 == 0 for x in [game(t) for t in [h + 1, h + 2, h * 3]])) * min([x for x in [game(t) for t in [h + 1, h + 2, h * 3]] if x % 2 == 0], default=0) + (1 - any(x % 2 == 0 for x in [game(t) for t in [h + 1, h + 2, h * 3]])) * max([game(t) for t in [h + 1, h + 2, h * 3]], default=0))
for i in range(50, 0, -1): print(i, game(i))