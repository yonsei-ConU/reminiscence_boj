import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N, M = minput()
memory_temp = list(minput())
cost_temp = list(minput())
apps = []
for i in range(N):
    if cost_temp[i] == 0:
        M -= memory_temp[i]
    else:
        apps.append([cost_temp[i], memory_temp[i]])

dp = [[0] * (sum(cost_temp) + 1) for _ in range(len(apps))]
for i in range(len(apps)):
    cost, memory = apps[i]
    
