import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
B = list(minput())
if set(A) != set(B): exit(print(0))

S = sorted(A)
for idx in range(N - 1, -1, -1):
    if B[idx] != S[idx]:
        break

idx += 1
if idx == N:
    val = 2 * 10 ** 9
else:
    val = S[idx]

lst = [i for i in A if i < val] + S[idx:]
# print(lst)
ans = 0
for i in range(idx - 1):
    if lst == B:
        ans = 1
        break
    if lst[i] > lst[i + 1]:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]

print(ans)
