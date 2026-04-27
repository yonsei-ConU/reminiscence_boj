import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
S = deque([input_().rstrip() for _ in range(N)])
ans = []
while S:
    if S[0] < S[-1]:
        ans.append(S.popleft())
    elif S[0] > S[-1]:
        ans.append(S.pop())
    else:
        left = 1
        right = len(S) - 2
        while left < right and S[left] == S[right]:
            left += 1
            right -= 1
        if left < right and S[left] < S[right]:
            ans.append(S.popleft())
        else:
            ans.append(S.pop())

ptr = 0
while ptr < len(ans):
    print(''.join(ans[ptr:ptr + 80]))
    ptr += 80
