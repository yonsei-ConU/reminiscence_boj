#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string DNA;
    std::cin >> DNA;
    int N = DNA.size();
    std::vector<int> a, t, g, c;
    for (int i = 0; i < N; i++) {
        char s = DNA[i];
        if (s == 'a') a.push_back(i);
        else if (s == 't') t.push_back(i);
        else if (s == 'g') g.push_back(i);
        else c.push_back(i);
    }
    std::vector<std::vector<int>> dp(N, std::vector<int>(N, 0));
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if ((DNA[i] == 'a' && DNA[j] == 't') || (DNA[i] == 'g' && DNA[j] == 'c')) dp[i][j] = 2;
        }
    }
    for (int diff = 2; diff < N; diff++) {
        for (int i = 0; i + diff < N; i++) {
            int j = i + diff;
            if ((DNA[i] == 'a' && DNA[j] == 't') || (DNA[i] == 'g' && DNA[j] == 'c')) dp[i][j] = std::max(dp[i][j], dp[i + 1][j - 1] + 2);
            for (int k = i + 1; k < j; k++) {
                dp[i][j] = std::max(dp[i][j], dp[k][j] + dp[i][k]);
            }
        }
    }
    std::cout << dp[0][N - 1];
    return 0;
}
