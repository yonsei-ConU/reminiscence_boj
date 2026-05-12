import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def step5(fish):
    # 5-1. INITALIZE DELTA WITH ALL 0
    delta = [lst[:] for lst in fish]
    for i in range(len(delta)):
        for j in range(len(delta[i])):
            delta[i][j] = 0

    # 5-2. FILL DELTA VALUE
    for y in range(len(fish)):
        for x in range(len(fish[y])):
            for k in range(2):
                ny, nx = y + dy[k], x + dx[k]
                if 0 <= ny < len(fish) and 0 <= nx < len(fish[ny]):
                    d = (fish[y][x] - fish[ny][nx])
                    if d >= 0:
                        d //= 5
                    else:
                        d = -(-d // 5)
                    delta[y][x] -= d
                    delta[ny][nx] += d

    # 5-3. MERGE FISH VALUE AND DELTA VALUE
    for i in range(len(fish)):
        for j in range(len(fish[i])):
            fish[i][j] += delta[i][j]


def step6(fish):
    new_fish = []
    for lst in fish:
        for val in lst:
            new_fish.append([val])
    fish, new_fish = new_fish, fish
    return fish


dy = [1, 0]
dx = [0, 1]

# 0. GET INPUT
N, K = minput()
fish = []
for val in list(minput()):
    fish.append([val])

ans = 0
while True:
    # 1. FIND MIN, MAX VALUE
    min_val = 999999999
    max_val = -999999999
    for val in fish:
        min_val = min(min_val, val[0])
        max_val = max(max_val, val[0])
    if max_val - min_val <= K:
        break
    ans += 1

    # 2. ADD ONE FISH TO SMALLEST
    for val in fish:
        if val[0] == min_val:
            val[0] += 1
    # print("Step 2", fish)

    # 3. STACK LEFTMOST FISH TANK
    f0 = fish[0][0]
    fish = fish[1:]
    fish[0].append(f0)
    # print("Step 3", fish)

    # 4. FLOAT AND ROTATE FISH TANK
    while True:
        # 4-1. CHECK WHETHER TO FLOAT AGAIN
        new_fish = []
        floating = []
        max_floating = 0
        for val in fish:
            if len(val) == 1:
                new_fish.append(val)
            else:
                floating.append(val)
                max_floating = max(max_floating, len(val))
        if max_floating > len(new_fish):
            break

        # 4-2. MOVE FISH TANK
        for lst in floating[::-1]:
            for i in range(len(lst)):
                new_fish[i].append(lst[i])
        fish, new_fish = new_fish, fish
    # print("Step 4", fish)

    # 5. ADJUST FISH COUNTS
    step5(fish)
    # print("Step 5", fish)

    # 6. PUT FISH TANKS ON FLOOR
    fish = step6(fish)
    # print("Step 6", fish)

    # 7. FLOAT AND ROTATE FISH TANK 2
    for _ in range(2):
        floating = fish[:(len(fish) >> 1)][::-1]
        for i in range(len(floating)):
            floating[i] = floating[i][::-1]
        fish = fish[len(fish) >> 1:]
        for i in range(len(fish)):
            fish[i].extend(floating[i])
    # print("Step 7", fish)

    step5(fish)
    # print("Step 8", fish)
    fish = step6(fish)
    # print("Step 9", fish)

print(ans)
