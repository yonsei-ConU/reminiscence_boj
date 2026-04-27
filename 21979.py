import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    s = input_().rstrip()
    ans = 0

    for mask in range(1 << (len(s) - 1)):
        i = 1
        m = mask
        cuts = [0]
        while m:
            if m & 1:
                cuts.append(i)
            i += 1
            m >>= 1
        tmp = [s[cuts[i]:cuts[i+1]] for i in range(len(cuts) - 1)]
        tmp.append(s[cuts[-1]:])
        real = [int(tmp[i], 16) for i in range(len(tmp))]
        ans += real == sorted(real)

    print(ans)
