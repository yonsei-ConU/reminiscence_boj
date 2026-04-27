import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())

pxor = [0]
cur_xor = 0
for i in range(N):
    cur_xor ^= A[i]
    pxor.append(cur_xor)

i = 1
ans = 0
while i < 10 ** 8:
    ps = [0]
    cur_sum = 0
    for j in range(2, N + 1)[::-1]:
        cur_sum += pxor[j] & i
        ps.append(cur_sum)
    ps.reverse()
    ans += ps[0]
    for j in range(1, N - 1):
        if pxor[j] & i:
            ans += (N - j - 1) * i - ps[j]
        else:
            ans += ps[j]
    i <<= 1

print(ans + sum(A))
