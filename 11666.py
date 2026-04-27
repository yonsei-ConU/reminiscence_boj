import sys
from heapq import heappop, heappush
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, m = minput()
researcher = [tuple(minput()) for _ in range(n)]
researcher.sort()
ans = 0
workstation = []

for a, s in researcher:
    if not workstation or workstation[0] > a:
        heappush(workstation, a + s)
    else:
        while workstation:
            t = heappop(workstation)
            if a <= t + m:
                break
        else:
            ans -= 1
        ans += 1
        heappush(workstation, a + s)

print(ans)
