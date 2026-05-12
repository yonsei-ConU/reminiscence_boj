from random import randint

data = open('data.txt', 'w')

N = 100000
data.write(str(N))
data.write('\n')

for i in range(2, N + 1):
    par = randint(1, i - 1)
    data.write(str(i) + ' ' + str(par) + ' ' + str(randint(1, 1000000)))
    data.write('\n')

M = 100000
data.write(str(M))
data.write('\n')
for i in range(M):
    q = randint(1, 2)
    if q == 1:
        r = randint(1, N - 1)
        s = randint(1, 1000000)
    else:
        r = randint(1, N)
        s = randint(1, N)
    data.write(str(q) + ' ' + str(r) + ' ' + str(s))
    data.write('\n')

data.close()
