import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def place_block(where, x_coordinates, y_count, block_num):
    # Note that X, Y coordinate is REVERSED, but albano?
    global score

    # 1. DETERMINE WHERE TO PLACE
    y_candidate = [False] * 6
    for y in range(5, 0, -1):
        check = True
        for x in x_coordinates:
            if where[y][x] or (y_count == 2 and where[y - 1][x]):
                check = False
                break
        if check:
            y_candidate[y] = True
    for y in range(5):
        if y_candidate[y] and not y_candidate[y + 1]:
            break
    else:
        y = 5

    # 2. ACTUALLY PLACE BLOCKS
    for x in x_coordinates:
        where[y][x] = block_num
        if y_count == 2:
            where[y - 1][x] = block_num

    while 1:  # AT MOST 6? LOOPS
        # 3. REMOVE BLOCKS
        removed = False
        for y in range(6):
            if 0 not in where[y]:
                where[y] = [0, 0, 0, 0]
                score += 1
                removed = True

        if removed:
            # 4. DROP BLOCKS
            for y in range(4, -1, -1):
                for x in range(4):
                    if not where[y][x] or where[y + 1][x]: continue
                    # here, there is a block in current position
                    # and there is no block in direct below pos
                    t = where[y][x]
                    if x and t == where[y][x - 1]: continue
                    elif x == 3 or t != where[y][x + 1]:
                        where[y][x] = 0
                        y_ = y
                        while y_ < 5 and not where[y_ + 1][x]:
                            y_ += 1
                        where[y_][x] = t
                    elif where[y + 1][x + 1]: continue
                    else:
                        where[y][x] = where[y][x + 1] = 0
                        y_ = y
                        while y_ < 5 and not where[y_ + 1][x] and not where[y_ + 1][x + 1]:
                            y_ += 1
                        where[y_][x] = t
                        where[y_][x + 1] = t

        # 5. PROCESS BRIGHT SPACE
        to_remove = bool(sum(where[0])) + bool(sum(where[1]))
        for i in range(to_remove):
            where.pop()
            where.appendleft([0, 0, 0, 0])

        if not removed: break


# 0. PREPROCESS
N = int(input_())
green = deque([[0, 0, 0, 0] for _ in range(6)])
blue = deque([[0, 0, 0, 0] for _ in range(6)])
score = 0

for i in range(1, N + 1):
    t, x, y = minput()
    if i == 8:
        1
    if t == 1:
        place_block(green, [y], 1, i)
        place_block(blue, [x], 1, i)
    elif t == 2:
        place_block(green, [y, y + 1], 1, i)
        place_block(blue, [x], 2, i)
    else:
        place_block(green, [y], 2, i)
        place_block(blue, [x, x + 1], 1, i)
    """print(f"iteration {i}")
    print('Green')
    for _ in green: print(*_)
    print('blue')
    for _ in blue: print(*_)"""

print(score)
g = 0
for _ in green: g += sum(map(bool, _))
for _ in blue: g += sum(map(bool, _))
print(g)
