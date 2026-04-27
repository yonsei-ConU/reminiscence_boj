import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dnc(seq):
    if len(seq) == 1:
        return True
    left = seq[:len(seq) >> 1][::-1]
    right = seq[(len(seq) >> 1) + 1:]
    assert len(left) == len(right)
    for i in range(len(left)):
        if left[i] == right[i]:
            return False
    return dnc(left[::-1]) and dnc(right)


for _ in range(int(input_())):
    ans = dnc(input_().rstrip())
    print("YES" if ans else "NO")
