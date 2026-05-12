import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    q, *query = list(minput())
    if q == 1:
        n, x, y = query
        x -= 1; y -= 1
        deg = min(x, n - 1 - x, y, n - 1 - y)
        delta = deg * 4 * (2 * (n >> 1) - deg + 1) + 1
        x -= deg
        y -= deg
        side_len = n - 1 - deg * 2
        if not x:
            print(delta + y)
        elif y == side_len:
            print(delta + side_len + x)
        elif x == side_len:
            print(delta + 3 * side_len - y)
        else:
            print(delta + 4 * side_len - x)
    else:
        n, z = query
        left = 0
        right = n // 2
        deg = 0
        while left <= right:
            mid = (left + right) // 2
            current_delta = mid * 4 * (2 * (n // 2) - mid + 1) + 1
            next_delta = (mid + 1) * 4 * (2 * (n // 2) - (mid + 1) + 1) + 1
            if current_delta <= z < next_delta:
                deg = mid
                break
            elif z < current_delta:
                right = mid - 1
            else:
                left = mid + 1
        else:
            deg = n // 2

        delta = deg * 4 * (2 * (n // 2) - deg + 1) + 1
        relative = z - delta
        side_len = n - 2 * deg - 1

        if not side_len:
            x = y = deg
        else:
            if relative < side_len:
                x = deg
                y = deg + relative
            elif relative < 2 * side_len:
                x = deg + (relative - side_len)
                y = n - 1 - deg
            elif relative < 3 * side_len:
                x = n - 1 - deg
                y = n - 1 - deg - (relative - 2 * side_len)
            else:
                x = n - 1 - deg - (relative - 3 * side_len)
                y = deg
        print(x + 1, y + 1)
