import sys
from heapq import *
q=sys.stdin.readline
N=int(q())
ans=0
cows=[]
for i in range(N):
 a,t=map(int,q().split())
 cows.append([a, t, i])
cows.sort(reverse=True)
heap = []
time = 0
while cows or heap:
 if not heap: time = max(time, cows[-1][0])
 while cows and cows[-1][0] <= time: heappush(heap, cows.pop()[::-1])
 _, t, a = heappop(heap)
 ans = max(ans, time - a)
 time += t
print(ans)
