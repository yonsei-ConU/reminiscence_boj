import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def suffix_array(S):
    ret = list(range(len(S)))
    rank = [ord(i) for i in S]
    tmp = [0] * len(S)
    k = 1
    while k < len(S):
        ret.sort(key=lambda i: (rank[i], rank[i + k] if i + k < len(S) else -1))
        tmp[ret[0]] = 0
        for i in range(1, len(S)):
            prev = ret[i - 1]
            cur = ret[i]
            tmp[cur] = tmp[prev] + ((rank[cur], rank[cur + k] if cur + k < len(S) else -1) != (rank[prev], rank[prev + k] if prev + k < len(S) else -1))
        tmp, rank = rank, tmp
        k <<= 1
    return ret


S = input_().rstrip()
sa = suffix_array(S)
for value in sa:
    print(value)
