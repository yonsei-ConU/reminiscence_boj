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
            if temp[mid] < element:
                lo = mid
            else:
                hi = mid
        if hi == len(temp):
            temp.append(element)
        else:
            temp[hi] = element
    return len(temp) - 1


def LDS_len(arr):
    temp = [-float('inf')]
    for element in arr:
        lo = -1
        hi = len(temp)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if temp[mid] > element:
                lo = mid
            else:
                hi = mid
        if hi == len(temp):
            temp.append(element)
        else:
            temp[hi] = element
    return len(temp) - 1


N = int(input_())
seq = list(minput())
print(max([LIS_len(seq[:i+1]) + LDS_len(seq[i:]) for i in range(N)]))
