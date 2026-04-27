import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, H = minput()
H = min(N, H)
dydaor = input_().rstrip()
if H == 1:
    print(0)
elif H == 2:
    i = 0
    ans = 0
    while i < N - 1:
        if dydaor[i] == dydaor[i + 1]:
            ans += 1
            i += 1
        i += 1
    print(ans)
elif H == 3:
    ans = N + 1
    for string in ["SRW", "SWR", "RSW", "RWS", "WSR", "WRS"]:
        ans = min(ans, sum(dydaor[i] != string[i % 3] for i in range(N)))
    print(ans)
else:
    print(-1)
