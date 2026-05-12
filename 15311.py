import random


def check(lst):
    assert len(lst) <= 2000
    psum = [0]
    for i in range(len(lst)):
        psum.append(psum[-1] + lst[i])
    chk = [False] * 1000000
    for i in range(len(psum)):
        for j in range(i + 1, len(psum)):
            x = psum[j] - psum[i]
            if x <= 1000000:
                chk[x - 1] = True
    return sum(chk)


lst = [1000] * 1000 + [1] * 1000
print(check(lst))
print(*lst)
