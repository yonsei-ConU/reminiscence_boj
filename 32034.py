import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    N = int(input_())
    S = input_().rstrip()
    odd = []
    even = []
    o = e = 0
    for i in range(N):
        if S[i] == 'T':
            if i & 1:
                odd.append(i)
                o += 1
            else:
                even.append(i)
                e += 1
    if o != e:
        print(-1)
    else:
        print(sum(abs(even[i] - odd[i]) for i in range(o)))
