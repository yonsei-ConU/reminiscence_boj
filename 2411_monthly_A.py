import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
tmp = [1]
for i in range(1, N):
    print(f'? {i} * {i + 1}', flush=True)
    x = input_().rstrip()
    if x == '-':
        tmp.append(-tmp[-1])
    else:
        tmp.append(tmp[-1])

d = 1
i = 1
for idx in range(1, N):
    if tmp[idx] == 1:
        break
else:
    d *= -1
    i = 2
    for idx in range(2, N):
        if tmp[idx] == -1:
            break
    else:
        assert False

print(f'? {i} + {idx + 1}', flush=True)
x = input_().rstrip()
if x == '+':
    d *= 1
else:
    d *= -1

ans = []
for i in range(N):
    if tmp[i] * d > 0:
        ans.append('+')
    else:
        ans.append('-')

print(f'! {" ".join(ans)}', flush=True)
