import sys
input_ = sys.stdin.readline
def minput():return map(int, input_().split())

from collections import deque
for _ in range(int(input_())):
    N, M = minput()
    importance = deque(minput())
    ans = 0
    check = {x: 0 for x in range(1, 10)}
    for i in importance:
        check[i] += 1
    while importance:
        next_print = importance.popleft()
        i = 9
        while i > next_print:
            if check[i] > 0:
                printed = False
                break
            i -= 1
        else:
            printed = True
        if not printed:
            importance.append(next_print)
            if M == 0:
                M = len(importance) - 1
            else:
                M -= 1
        else:
            ans += 1
            check[next_print] -= 1
            if M == 0:
                print(ans)
                break
            else:
                M -= 1
