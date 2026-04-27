def minput(): return map(int, input().split())

N, K = minput()
S = list(minput())
seq = []

cnt = 0
for i in range(N):
    if not s[i] % 2:
        cnt += 1
    else:
        if cnt:
            seq.append(cnt)
        cnt = 0

start = 0
end = 0
ans = seq[0]

