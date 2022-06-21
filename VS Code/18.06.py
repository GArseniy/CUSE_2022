from functools import lru_cache

def moves(h):
	a, b = h
	return ((a, b+2), (a, b*2), (a*2, b), (a+2, b))

@lru_cache(None)
def game(h):
	if sum(h) >= 79:
		return 0
	steps = [game(x) for x in moves(h)]
	if any(x%2 == 0 for x in steps):
		return 1 + min(x for x in steps if x%2 ==0)
	return 1 + max(steps)

for i in range(1, 71):
	print(i, game((9, i)))

while True:
	c = 0