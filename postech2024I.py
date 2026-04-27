import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_())
H = list(minput())
scores = list(minput())
durablity = list(minput())

maximum_scores = [0]
dp = [0]

for i in range(N - 1):
    score = scores[i]
    threshold = durablity[i] + H[i + 1]
    lo = -1
    hi = i + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if H[mid] >= threshold:
            lo = mid
        else:
            hi = mid
    if lo != -1:
        dp.append(maximum_scores[lo] + score)
        maximum_scores.append(max(maximum_scores[-1], dp[-1]))
    else:
        dp.append(0)
        maximum_scores.append(maximum_scores[-1])

print(maximum_scores[-1])
