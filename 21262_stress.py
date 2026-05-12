import random
from math import gcd

def solve(n, k):
    ans = list(range(1, n + 1))
    if not k % 2:
        ans[0] = n
        ans[-1] = 1
    for i in range(((k - 1) >> 1)):
        idx = i * 2 + 1
        ans[idx], ans[idx + 1] = ans[idx + 1], ans[idx]
    return ans


try:
    for i in range(1, 10001):
        n = random.randint(1, 100000)
        k = random.randint(1, n)
        p = solve(n, k)
        if sum(1 for i in range(n) if gcd(p[i], i + 1) == 1) != k:
            print(f"Test case #{i} failed")
            print(f"Input {n} {k}")
            # print(f"Output: {p}")
            print(f"Expected: {k}")
            print(f"Received: {sum(1 for i in range(n) if gcd(p[i], i + 1) == 1)}")
            break
    else:
        print(f"10000 Test cases passed")
except KeyboardInterrupt:
    print(f"Stopping. Currently {i} Test cases passed")
