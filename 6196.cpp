#include <iostream>
#include <vector>

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int mod = 100000000;
    int M, N;
    std::cin >> M >> N;
    std::vector<std::vector<int> > squares(M);

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            int t;
            std::cin >> t;
            squares[i].push_back(t);
        }
    }

    // dp[i][mask] = 위에서부터 i번줄까지, 마지막 줄에서 고른 게 mask
    int dp[M][1 << N];

    // 맨 윗줄 디피 테이블 초기화
    for (int mask = 0; mask < (1 << N); mask++) {
        bool chk = true;
        for (int j = 0; j < N; j++) {
            if (!squares[0][j] && mask & (1 << j)) {
                chk = false;
                break;
            }
        }
        if (mask & (mask << 1)) chk = false;
        if (chk) dp[0][mask] = 1;
        else dp[0][mask] = 0;
    }

    // 나머지 줄 만들기
    for (int i = 1; i < M; i++) {
        for (int mask = 0; mask < (1 << N); mask++) {
            bool chk = true;
            for (int j = 0; j < N; j++) {
                if (!squares[i][j] && mask & (1 << j)) {
                    chk = false;
                    break;
                }
                if (mask & (mask << 1)) chk = false;
            }
            dp[i][mask] = 0;
            if (!chk) continue;

            for (int prev_mask = 0; prev_mask < (1 << N); prev_mask++) {
                if (!(mask & prev_mask)) {
                    dp[i][mask] += dp[i - 1][prev_mask];
                }
            }
            dp[i][mask] %= mod;
        }
    }

    int ans = 0;
    for (int mask = 0; mask < (1 << N); mask++) {
        ans += dp[M - 1][mask];
        ans %= mod;
    }

    std::cout << ans;
    return 0;
}
