#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int A, B, C;
    std::cin >> A >> B >> C;
    std::string X, Y;
    std::cin >> X >> Y;
    int N = X.size();
    int M = Y.size();
    std::vector<std::vector<int>> dp(N + 1, std::vector<int>(M + 1, -998244353));
    dp[0][0] = 0;
    for (int i = 1; i <= N; i++) {
        dp[i][0] = i * B;
    }
    for (int j = 1; j <= M; j++) {
        dp[0][j] = j * B;
    }
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = std::max(dp[i][j], dp[i - 1][j - 1] + A);
            } else {
                dp[i][j] = std::max(dp[i][j], dp[i - 1][j - 1] + C);
            }
            dp[i][j] = std::max(dp[i][j], dp[i - 1][j] + B);
            dp[i][j] = std::max(dp[i][j], dp[i][j - 1] + B);
        }
    }
    std::cout << dp[N][M];
    return 0;
}
