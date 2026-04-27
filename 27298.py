import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


numbers = [0b111111, 10, 0b1011101,
    0b1001111, 0b1101010, 0b1100111,
    0b1110111, 11, 127, 0b1101011]
ans = [{(i,)} for i in range(10)]
for m in range(1, 10):
    for n in range(m, 10):
        for o in range(n, 10):
            for p in range(o, 10):
                for q in range(p, 10):
                    for r in range(q, 10):
                        for s in range(r, 10):
                            for t in range(s, 10):
                                for u in range(t, 10):
                                    for v in range(u, 10):
                                        try:
                                            idx = numbers.index(numbers[m] ^ numbers[n] ^ numbers[o] ^ numbers[p] ^ numbers[q] ^ numbers[r] ^ numbers[s] ^ numbers[t] ^ numbers[u] ^ numbers[v])
                                            tmp = [m, n, o, p, q, r, s, t, u, v]
                                            tmp2 = []
                                            for i in range(10):
                                                if tmp.count(i) & 1:
                                                    tmp2.append(i)
                                            ans[idx].add(tuple(tmp2))
                                        except:
                                            pass

print(*ans, sep='\n')
