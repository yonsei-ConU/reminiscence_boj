import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, K = minput()
cards = sorted(list(minput())) + [9999999999]
ans = [-1] * (N + 1)
ptr = 0
for i in range(N + 1):
    if ptr ^ M and cards[ptr] == i:
        ptr += 1
    ans[i] = ptr

used = set()
output = []
for query in list(minput()):
    x = ans[query]
    while cards[x] in used:
        x += 1
        if x == M: assert False
    output.append(str(cards[x]))
    used.add(cards[x])

sys.stdout.write('\n'.join(output))
