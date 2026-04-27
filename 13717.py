import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans_val = 0
ans_name = ''
ans_sum = 0

for _ in range(N):
    name = input_().strip()
    if not ans_name: ans_name = name
    K, M = minput()
    tmp = 0
    while M >= K:
        ev = M // K
        tmp += ev
        M %= K
        M += 2 * ev
    if tmp > ans_val:
        ans_val = tmp
        ans_name = name
    ans_sum += tmp

print(ans_sum)
print(ans_name)
