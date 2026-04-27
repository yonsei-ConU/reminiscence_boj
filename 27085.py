import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, s = minput()
s -= 1
A = list(minput())
left = s - 1
right = s + 1
score = 0

while left >= 0:
    if A[left] >= 0:
        score += A[left]
        left -= 1
    else:
        break
while right < N:
    if A[right] >= 0:
        score += A[right]
        right += 1
    else:
        break

choice = []
cur_sum = 0
while left >= 0:
    if A[l
