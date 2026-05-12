import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, H_atk = minput()
dungeon = [tuple(minput()) for _ in range(N)]

lo = 0
hi = 10 ** 18

while lo + 1 < hi:
    mid = (lo + hi) >> 1
    hp = mid
    atk = H_atk
    check = True

    for t, a, h in dungeon:
        if t == 1:
            attack_count = (h - 1) // atk
            hp -= attack_count * a
            if hp <= 0:
                check = False
                break

        else:
            hp = min(mid, hp + h)
            atk += a

    if check:
        hi = mid
    else:
        lo = mid

print(hi)
