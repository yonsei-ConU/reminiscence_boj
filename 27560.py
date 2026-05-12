import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput()) + [0]
S = sum(A)
rightmost = N
ans = []
cur = 0
direction = 'R'
while S:
    if direction == 'R':
        if cur == rightmost:
            direction = 'L'
        else:
            ans.append(direction)
            A[cur] -= 1
            S -= 1
            cur += 1
    else:
        if A[cur - 1] > 1:
            ans.append(direction)
            A[cur - 1] -= 1
            S -= 1
            cur -= 1
        elif A[cur]:
            direction = 'R'
        else:
            ans.append(direction)
            A[cur - 1] -= 1
            S -= 1
            cur -= 1
            rightmost -= 1

print(''.join(ans))
