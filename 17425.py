import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def sieve(n):
    ret = [0] * n
    for i in range(n):
        for j in range(i + 1, n, i + 1):
            ret[j] += i + 1
    return ret


orig = sieve(1000001)
ps = [0]
cur_sum = 0
for i in range(1000001):
    cur_sum += orig[i]
    ps.append(cur_sum)

for _ in range(int(input_())):
    print(ps[int(input_()) + 1])
