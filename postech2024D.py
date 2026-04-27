import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, K = minput()
S = list(input_().rstrip())
k = 0
start = 0
end = N - 1
while k < K and 0 <= start < end < N:
    if S[start] == 'C':
        while 0 <= start < end < N and S[end] == 'C':
            end -= 1
        if 0 <= start < end < N:
            S[start], S[end] = S[end], S[start]
            k += 1
    else:
        start += 1

ans = 0
p = 0
for i in range(N):
    if S[i] == 'P':
        p += 1
    else:
        ans += p * (p - 1) // 2

print(ans)
