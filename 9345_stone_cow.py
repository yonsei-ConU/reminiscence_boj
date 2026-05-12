import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def square_sum(n):
    return n*(n+1)*(2*n+1) //6

def init(start, end, index):
    if start == end:
        tree[index] = (arr[start])**2
        return
    mid = (start + end) // 2
    init(start, mid, index*2)
    init(mid+1, end, index*2+1)
    tree[index] = tree[index*2] + tree[index*2+1]
    return


def query(start, end, index, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return tree[index]
    mid = (start + end) // 2
    return query(start, mid, index*2, left, right) + query(mid+1, end, index*2+1, left, right)

def update(start, end, index, i, value):
    if start == end and start == i:
        tree[index] = value
        return
    if start > i or end < i:
        return
    mid = (start + end) // 2
    update(start, mid, index*2, i, value)
    update(mid+1, end, index*2+1, i, value)
    tree[index] = tree[index*2] + tree[index*2+1]
    return


t = int(ipt())
for _ in range(t):
    n, k = minput()
    tree = [0]*2*2**math.ceil(math.log(n, 2))
    arr = [i for i in range(n)]
    random.shuffle(arr)
    init(0, n-1, 1)
    for _ in range(k):
        a, b, c = minput()
        s = query(0, n-1, 1, b, c)
        ss = square_sum(c) - square_sum(b-1)
        if a == 1:
            if s == ss:
                print('YES')
            else:
                print('NO')
        elif a == 0:
            p = query(0, n-1, 1, b, b)
            q = query(0, n-1, 1, c, c)
            update(0, n-1, 1, b, q)
            update(0, n-1, 1, c, p)