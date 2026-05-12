import io, os
from collections import deque
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
INF = 10 ** 18
B = int(input_())
k = int(input_())
items = []  # (advertised, real)
total_items = []
for _ in range(k):
    cnt, *package = minput()
    package = iter(package)
    if not items:
        for p in package:
            items.append((p, p))
            total_items.append((p, p))
        continue
    # dp[i][j] = (i번째 아이템까지만 보고 광고된 가치가 j일 때 실제 가치의 최솟값)
    dp = [[INF] * 2001 for _ in range(len(items) + 1)]
    dp[0][0] = 0
    for i in range(1, len(items) + 1):
        advertised, real = items[i - 1]
        for j in range(2001):
            dp[i][j] = dp[i - 1][j]
            k_ = j - advertised
            l = real
            while k_ >= 0:
                if dp[i - 1][k_] + l >= j:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k_] + l)
                k_ -= advertised
                l += real
    cur = deque()
    nxt_i = next(package)
    items = []
    for i in range(2001):
        if i == nxt_i:
            cur.append(i)
            try:
                nxt_i = next(package)
            except:
                nxt_i = 2001
        if dp[-1][i] != INF:
            while cur and cur[0] <= i:
                items.append((cur[0], dp[-1][i]))
                total_items.append((cur[0], dp[-1][i]))
                cur.popleft()

ans = INF
for advertised, real in total_items:
    if real >= B:
        ans = min(ans, advertised)
if ans == INF:
    output.append('impossible')
else:
    output.append(str(ans))
os.write(1, '\n'.join(output).encode())
os._exit(0)
