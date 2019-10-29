import random
import sys

def die():
    return random.randrange(1, 7)

def twodice():
    while True:
        d1 = die()
        d2 = die()
        if d1 == d2 and d1 != 1:
            continue
        return (d1, d2)

def ps(n):
    rs = 0
    for _ in range(n):
        if twodice() == (1, 1):
            rs += 1
    return rs / n

print(ps(int(sys.argv[1])))
