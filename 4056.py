def is_valid(location, num):
    y, x = location // 9, location % 9
    if (1 << num) & hori[x]: return False
    if (1 << num) & vert[y]: return False
    if (1 << num) & square[y // 3 * 3 + x // 3]: return False
    return True


def solve(idx):
    if idx == len(zeros):
        return True
    location = zeros[idx]
    y, x = location // 9, location % 9
    for num in range(1, 10):
        if is_valid(location, num):
            sdk[y][x] = num
            hori[x] |= 1 << num
            vert[y] |= 1 << num
            square[y // 3 * 3 + x // 3] |= 1 << num
            if solve(idx + 1):
                return True
            hori[x] ^= 1 <<num
            vert[y] ^= 1 <<num
            square[y // 3 * 3 + x // 3] ^= 1 << num
            sdk[y][x] = 0
    return False


for _ in range(int(input())):
    sdk = [list(map(int, list(input()))) for _ in range(9)]
    zeros = []
    hori = [0] * 9
    vert = [0] * 9
    square = [0] * 9
    for loc in range(81):
        tmp = sdk[loc//9][loc%9]
        if not tmp:
            zeros.append(loc)
        else:
            vert[loc // 9] |= 1 << tmp
            hori[loc % 9] |= 1 << tmp
            square[loc // 27 * 3 + loc % 9 // 3] |= 1 << tmp
    chk = solve(0)
    for loc in range(81):
        t = sdk[loc // 9][loc % 9]
        sdk[loc // 9][loc % 9] = 0
        if not is_valid(loc, t):
            chk = False
            break
        sdk[loc // 9][loc % 9] = t
    if chk:
        for l in sdk: print(*l, sep='')
    else:
        print("Could not complete this grid.")
    print()
