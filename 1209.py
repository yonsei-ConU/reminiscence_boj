import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
"""
### sol by JYJin

일단, 단조증가 수열이랑 단조감소 수열을 그냥 따로 해 보면 되긴 함.
겹치는 게 많은 경우가 최적이다. (Intuitive)
dp[idx][k]를 0 ~ idx번째까지 채우고 B의 인덱스가 k일 때의 최솟값???
WLOG, 증가하는 경우만 살펴본다.
기본적으로 추가되는 상수는 |A_idx - k|
dp[idx - 1][k_] (k_ <= k)일 때 저 값들 중 최솟값에다가 A_idx - k를 더하면 그게 dp[idx][k]?????? 여긴 좀더 생각해보자.
물론 좌압 필요함.
상태는 O(N2)개, 전이를 N번 하므로 시복이 세제곱...?
가능한 최적화 방법...? 상태전이 부분에서 prefix min을 사용하면 된다 -> 처리과정 O(N2), 상태전이 쿼리당 O(1)이므로 O(N2)에 해결가능.

참고: https://www.acmicpc.net/problem/13323 부등호가 없고 N이 100만??????
slope trick이라는 게 있대요
"""
