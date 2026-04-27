import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dist(p1, p2):
    assert not len(p1) - len(p2)
    return sum((p2[i] - p1[i]) ** 2 for i in range(len(p1))) ** 0.5


def P3(x, y, z):
    if sum(i == 100 for i in [x, y, z]) >= 2:
        return 100 - min(x, y, z)
    elif x == 100:
        return dist((y, z), (100, 100))
    elif y == 100:
        return dist((x, z), (100, 100))
    elif z == 100:
        return dist((x, y), (100, 100))
    else:
        d1 = dist((x, y), (100, 100)) + 100 - z
        d2 = dist((x, z), (100, 100)) + 100 - y
        d3 = dist((y, z), (100, 100)) + 100 - x
        return min(d1, d2, d3)

print(P3(*minput()))
