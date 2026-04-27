import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
grundy = [0, 1, 1, 1, 2, 2]
for i in range(6, n + 1):
    a = i - 5
    b = 0
    next_state = {grundy[i - 3], grundy[i - 4]}
    while a >= b:
        next_state.add(grundy[a] ^ grundy[b])
        a -= 1
        b += 1
    mex = 0
    while mex in next_state:
        mex += 1
    grundy.append(mex)

print(2 - bool(grundy[n]))
