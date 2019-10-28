import random
import sys

def die():
    return random.randrange(1, 7)

def p7(n):
    r7 = 0
    for _ in range(n):
        if die() + die() == 7:
            r7 += 1
    return r7 / n

print(p7(int(sys.argv[1])))
