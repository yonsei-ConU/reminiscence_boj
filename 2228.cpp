#include <iostream>
#include <vector>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    std::vector<int> A(N);
    for (auto &i : A) std::cin >> i;
    // dp[i][j]: until A[i], j rnrks
    std::vector<std::vector<int>> dp0(N + 1, std::vector<int>(M + 1, -100000000));
    std::vector<std::vector<int>> dp1(N + 1, std::vector<int>(M + 1, -100000000));
    dp1[0][0] = 0;
    for (int i = 1; i <= N; i++) {
        int val = A[i - 1];
        dp1[i][0] = 0;
        for (int j = 1; j <= M; j++) {
            if (dp0[i - 1][j] != -100000000) {
                dp0[i][j] = std::max(dp0[i][j], dp0[i - 1][j] + val);
            }
            if (i >= 2 && dp1[i - 2][j - 1] != -100000000) {
                dp0[i][j] = std::max(dp0[i][j], dp1[i - 2][j - 1] + val);
            } else if (i == 1 && j == 1) {
                dp0[i][j] = std::max(dp0[i][j], val);
            }
            dp1[i][j] = std::max(dp1[i - 1][j], dp0[i][j]);
        }
    }
    int ans = -1000000000;
    for (int i = 0; i <= N; i++) {
        ans = std::max(ans, dp1[i][M]);
    }
    std::cout << ans;
    return 0;
}
