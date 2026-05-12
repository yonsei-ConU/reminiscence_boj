import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
stamp = input_().rstrip()

J = O = I = 0
ps = [[0, 0, 0] for _ in range(N)]

if stamp[0] == 'J':
    ps[0] = [1, 0, 0]
    J += 1
elif stamp[0] == 'O':
    ps[0] = [0, 1, 0]
    O += 1
elif stamp[0] == 'I':
    ps[0] = [0, 0, 1]
    I += 1

for i in range(1, N):
    if stamp[i] == 'J':
        nxt = [1, 0, 0]
        J += 1
    elif stamp[i] == 'O':
        nxt = [0, 1, 0]
        O += 1
    else:
        nxt = [0, 0, 1]
        I += 1

    for j in range(3):
        ps[i][j] = ps[i - 1][j] + nxt[j]

cur_I = 0
ans_default = 0
for i in range(N):
    if stamp[i] == 'O':
        cur_I += I - ps[i][2]
        ans_default += ps[i][0] * (I - ps[i][2])
cur_J = 0

ans = 0
for i in range(N):
    # J
    ans = max(ans, cur_I)
    # O
    ans = max(ans, (ps[i - 1][0] if i else 0) * (I - (ps[i - 1][2] if i else 0)))
    # I
    ans = max(ans, cur_J)

    if stamp[i] == 'O':
        cur_J += ps[i][0]
        cur_I -= I - ps[i][2]

print(ans_default + max(ans, cur_J))
