from collections import deque

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = deque(sorted(a))
    ans = 0
    while a:
        t = a.popleft()
        if t != ans:
            break
        a.popleft()
        ans += 1
    print(ans)
