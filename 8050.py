import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def check(lst):
    for i in range(n - 1):
        if lst[i] == lst[i + 1]:
            return False
    ans = +(lst[1] > lst[0])
    for i in range(2, len(lst)):
        tmp = +(lst[i] > lst[i - 1])
        if not i & 1:
            tmp = 1 - tmp
        if not ans & tmp:
            return False
    return True


for _ in range(int(input_())):
    n = int(input_())
    h = [int(input_()) for _ in range(n)]
    h.sort()
    ans1 = []
    left = 0
    right = (n + 1) >> 1
    for i in range(n):
        if not i & 1:
            ans1.append(h[left])
            left += 1
        else:
            ans1.append(h[right])
            right += 1
    if check(ans1):
        print("TAK")
        continue
    ans2 = []
    left = n >> 1
    right = 0
    for i in range(n):
        if not i & 1:
            ans2.append(h[left])
            left += 1
        else:
            ans2.append(h[right])
            right += 1
    if check(ans2):
        print("TAK")
    else:
        print("NIE")
