import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def distinct_diff(vec):
    ret = set()
    for i in range(len(vec)):
        for j in range(i):
            ret.add(vec[j] - vec[i])
    return len(ret)


ans = [1]
for i in range(29):
    ans.append(ans[-1] * 2)
N = int(input_())
print(distinct_diff(ans[:N]))
print(*(ans[:N]))
print(N - 1)
print(*[i + 1 for i in range(N)])