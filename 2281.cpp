#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m;
    std::cin >> n >> m;
    std::vector<int> A(n);
    for (auto &i : A) {
        std::cin >> i;
    }
    // dp[i][j] = (i번째 이름까지 썼고 현재 줄 시작이 j번째 이름 -> 남는 칸 수 제곱 합 최소)
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 1000111100));
    dp[0][0] = 0;
    for (int i = 1; i < n; i++) {
        int sum = -1;
        for (int j = i - 1; j >= 0; j--) {
            sum += 1 + A[j];
            if (sum > m) break;
            else dp[i][i] = std::min(dp[i][i], dp[i - 1][j] + (m - sum) * (m - sum));
            if (sum + 1 + A[i] <= m) dp[i][j] = std::min(dp[i][j], dp[i - 1][j]);
        }
    }
    std::cout << *std::min_element(dp[n - 1].begin(), dp[n - 1].end());
    return 0;
}
