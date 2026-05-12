#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, M, P;
        std::cin >> N >> M >> P;
        std::vector<std::vector<int>> cost(P, std::vector<int>(2, 0));
        for (int i = 0; i < N; i++) {
            std::string s;
            std::cin >> s;
            for (int j = 0; j < P; j++) {
                if (s[j] == '0') cost[j][1]++;
                else cost[j][0]++;
            }
        }
        std::vector<std::string> forbidden(M);
        for (auto &i : forbidden) std::cin >> i;
        std::sort(forbidden.begin(), forbidden.end());
        // dp[i][j][k]: i번째 옵션까지 정했음, j ~ k번 forbidden 옵션에 해당 (단 dp[i][M - 1][M]은 그 구간이 없음을 표시) -> 불만 최솟값
        std::vector<std::vector<std::vector<int>>> dp(P + 1, std::vector<std::vector<int>>(M, std::vector<int>(M + 1, 999999999)));
        dp[0][0][M - 1] = 0;
        for (int i = 0; i < P; i++) {
            for (int j = 0; j < M; j++) {
                for (int k = j; k < M; k++) {
                    int lo = j - 1;
                    int hi = k + 1;
                    while (lo + 1 < hi) {
                        int mid = (lo + hi) >> 1;
                        if (forbidden[mid][i] == '1') hi = mid;
                        else lo = mid;
                    }
                    // lo번까지 0, hi번부터 1
                    // 다음 옵션 0 부여
                    if (lo == j - 1) {
                        dp[i + 1][M - 1][M] = std::min(dp[i + 1][M - 1][M], dp[i][j][k] + cost[i][0]);
                    } else {
                        dp[i + 1][j][lo] = std::min(dp[i + 1][j][lo], dp[i][j][k] + cost[i][0]);
                    }
                    // 다음 옵션 1 부여
                    if (hi == k + 1) {
                        dp[i + 1][M - 1][M] = std::min(dp[i + 1][M - 1][M], dp[i][j][k] + cost[i][1]);
                    } else {
                        dp[i + 1][hi][k] = std::min(dp[i + 1][hi][k], dp[i][j][k] + cost[i][1]);
                    }
                }
            }
            dp[i + 1][M - 1][M] = std::min(dp[i + 1][M - 1][M], dp[i][M - 1][M] + std::min(cost[i][0], cost[i][1]));
        }
        std::cout << "Case #" << t << ": " << dp[P][M - 1][M] << '\n';
    }
    return 0;
}