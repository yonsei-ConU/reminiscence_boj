import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K, M = minput()
if M + K > N + 1: exit(print(-1))
ans = [str(i) for i in range(N - K + 1, N + 1)]
# 남은 원소 개수는 N - K 개, 남은 뭉탱이 개수는 M - 1 개
# 한 뭉탱이당 최대 원소 개수는 K 개
element_left = N - K
MTE_left = M - 1
while element_left > MTE_left:
    MTE_size = min(K - 1, element_left - MTE_left) + 1
    tmp = [str(i) for i in range(element_left - MTE_size + 1, element_left + 1)]
    element_left -= MTE_size
    ans += tmp[::-1]

ans += [str(i) for i in range(1, element_left + 1)[::-1]]
print(' '.join(ans))
