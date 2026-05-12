#include <iostream>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int MX = 1000000000;
    int N, M;
    std::cin >> N >> M;
    int sum = 0;
    int dp[N + 1][M + 100000];
    int squares[N];
    for (int i = 0; i < N; i++) {
        int t;
        std::cin >> t;
        squares[i] = t;
        t *= t;
        sum += t;
    }
    for (int i = 0; i < N + 1; i++) {
        for (int j = 0; j < M + 100000; j++) dp[i][j] = MX;
    }
    dp[0][0] = 0;

    for (int i = 1; i < N + 1; i++) {
        int original_size = squares[i - 1];
        for (int j = 0; j < M + 100000; j++) {
            for (int k = 1; k <= 150; k++) {
                if (j + k * k >= M + 100000) break;
                else {
                    int cost = k - original_size;
                    cost *= cost;
                    dp[i][j + k * k] = std::min(dp[i][j + k * k], dp[i - 1][j] + cost);
                }
            }
        }
    }

    int ans = dp[N][M];
    if (ans == MX) std::cout << -1;
    else std::cout << ans;

    return 0;
}