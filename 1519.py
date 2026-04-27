import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def all_substrings(x):
    x = str(x)
    l = len(x)
    ret = []
    for i in range(l):
        for j in range(i + 1, l + 1):
            t = int(x[i:j])
            if t: ret.append(t)
    return sorted(set(ret))


N = int(input_())
grundy = [0] * 10
for n in range(10, N):
    # print('n', n)
    removable = all_substrings(n)
    removable.pop()
    # print('removable', removable)
    next_state = set()
    for x in removable:
        next_state.add(grundy[n - x])
    # print('next_state', next_state)
    mex = 0
    while mex in next_state:
        mex += 1
    # print('mex', mex)
    grundy.append(mex)
# print(grundy[10], grundy[16], grundy[17])
# N
removable = all_substrings(N)
removable.pop()
for x in removable:
    if not grundy[N - x]:
        print(x)
        break
else:
    print(-1)
