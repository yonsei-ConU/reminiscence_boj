import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    s = input_().rstrip()
    if s == '0':
        break
    N = len(s)
    # dp[mask][last] = (누른 글자 인덱스 집합이 mask이고 마지막 누른 글자 인덱스가 last일때 최소 횟수)
    dp = [[0] * N for _ in range(1 << N)]
    for mask in range(1 << N):
        
