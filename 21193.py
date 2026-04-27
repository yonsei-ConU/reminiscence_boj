import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
K = int(input_())
w = list(minput())
# dp[i][j] = (i번째 물건까지 봤을 때, 합이 j이면, 되나?)
