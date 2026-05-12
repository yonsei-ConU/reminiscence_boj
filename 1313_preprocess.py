def sieve(n):
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                a[j] = False
    return a


prime_check = sieve(10 ** 7)
print('sieve done')
ans = []
for i in range(100, 10 ** 7 + 1):
    if prime_check[i]:
        continue
    if i == 297:
        1
    si = str(i)
    l = len(si)
    chk = True
    for idx1 in range(l - 1):
        for idx2 in range(idx1 + 2, l + 1):
            if not idx1 and idx2 == l: continue
            if not prime_check[int(si[idx1:idx2])]:
                chk = False
                break
        if not chk: break
    if chk: ans.append(si)

outfile = open('data.txt', 'w')
outfile.write('[' + ', '.join(ans) + ']')
outfile.close()
