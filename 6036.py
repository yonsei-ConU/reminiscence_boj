import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
cur = (1 << N) - 1
s = []
s.append(cur)
for i in range(1, (1 << N)):
    least = 0
    while not 1 << least & i:
        least += 1
    cur ^= (1 << least)
    s.append(cur)

for element in s:
    res = []
    for i in range(N):
        if element & 1 << i:
            res.append('O')
        else:
            res.append('X')
    print(''.join(res))

print('O' * N)
