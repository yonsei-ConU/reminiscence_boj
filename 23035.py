import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def LIS_len(arr):
    temp = [-float('inf')]
    for element in arr:
        lo = -1
        hi = len(temp)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if temp[mid] <= element:
                lo = mid
            else:
                hi = mid
        if hi == len(temp):
            temp.append(element)
        else:
            temp[hi] = element
        print(temp)
    return len(temp) - 1


N, M = minput()
T = int(input_())
cats = []
for _ in range(T):
    r, c = minput()
    if 0 <= r <= N and 0 <= c <= M:
        cats.append([r, c])

cats.sort()
ans = LIS_len(cats)
cats = [[c[1], c[0]] for c in cats]
cats.sort()
print(max(LIS_len(cats), ans))
